from flask import Flask, render_template, request, url_for, redirect
from tinydb import TinyDB, Query, where
import arrow
import time


def insert_entry(d):
    # d is a dict, request.form

    # build -- or rebuild -- (entry) dict...
    entry = {
        'surname': (d.get('inputSurname', None)).strip(),
        'given': (d.get('inputGivenName', None)).strip(),
        'dob': d.get('inputDob', None),
        'overline': (d.get('inputOverline', None)).strip(),
        'content': (d.get('inputContent', None)).strip(),
        'modDate': arrow.utcnow().timestamp,
        'delete': False,
    }
    # get (draft) status: b/c this is a checkbox, value might not exist
    if d.get('draft'):
        entry['draft'] = True
    else:
        entry['draft'] = None

    # if (recordId) exists in form data then we are updating record, else inserting new record
    if d.get('recordId'):
        # it's a quirk that (doc_ids) must be a list even though we're updating 1 record
        res = db.update(entry, doc_ids=[int(d.get('recordId'))])
        return (res[0], entry['surname'])
    else:
        res = db.insert(entry)
        return (res, entry['surname'])


def entries():
    return db.all()


def entries_all():
    # entries with (deleted) is False
    return [item for item in db.all() if item['delete'] is False]


def entries_deleted():
    # entries with (deleted) is True
    return [item for item in db.all() if item['delete'] is True]


def entries_draft():
    # entries with (draft) is True, (deleted) is False
    return [item for item in db.all() if (item['delete'] is False) and (item['draft'] is True)]


def all_entries_short_sorted():
    records = entries()
    new_list = [{"id": item.doc_id, "name": item['surname'] + ", " + item['given'], "delete": item['delete'], "draft": item['draft']} for item in records]
    sorted_new_list = sorted(new_list, key=lambda k: k['name'])
    return sorted_new_list


def all_entry_ids():
    return [
        p.doc_id for p in entries_all()
    ]


def alpha_sort_all():
    # want sorted, unique list of first letters of surnames in db
    records = entries_all()
    letter_list = sorted(set([entry['surname'][0]for entry in entries_all()]))
    # create list of dicts in form { "letter": "c", "names": ["bob", "fred"] }
    data = [{'letter': item, 'names': []} for item in letter_list]
    for item in records:
        # gets dict from data list if dict's letter value is same as current item's surname slice
        matching_record = next(i for i in data if i['letter'] == item['surname'][0])
        the_name = item['surname'] + ", " + item['given']
        the_id = item.doc_id
        matching_record['names'].append({"name": the_name, "id": the_id})
    return data


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    result = None
    if request.method == 'POST':
        result = insert_entry(request.form)
    return render_template('add.html', result=result)


@app.route('/view')
def view():
    list_by_letter = alpha_sort_all()  # list of dicts
    list_sorted = all_entries_short_sorted()  # list of dicts
    template_data = {"list_by_letter": list_by_letter, "list_sorted": list_sorted}
    return render_template('view.html', data=template_data)


@app.route('/view/<int:record_id>', methods=['GET', 'POST'])
def view_entry(record_id):
    result = None
    if request.method == 'POST':
        if request.form['btn'] == 'delete':
            res = db.update({'delete': True}, doc_ids=[int(request.form.get('recordId'))])
            return redirect(url_for('browse'))
        else:
            result = insert_entry(request.form)
            time.sleep(1)
    template_data = db.get(doc_id=record_id)
    template_data['modDate'] = (arrow.get(template_data['modDate'])).to('US/Eastern').format('YYYY-MM-DD h:mm a')
    # print(template_data)
    return render_template('view_entry.html', data=template_data, result=result)


if __name__ == '__main__':
    app.run(debug=True)
