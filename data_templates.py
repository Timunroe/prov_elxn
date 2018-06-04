page_template = '''\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <title>Ontario Election 2018</title>
    <link rel="stylesheet" href="https://unpkg.com/tachyons@4.8.0/css/tachyons.min.css"/>
    <style type="text/css">
        $css
    </style>

</head>
    <body style="max-width: 800px;margin: auto;">
        $core
    </body>
</html
'''

core_template = '''\

{% macro show_post(item) %}
    <article class="pica-card pica-fade" style="margin-top: 18px;">
        {% if item['img_api'] != '' %}
        <div class="pica-card-image">
            <a class="pica-link" target="_blank" href="{{ item['link'] }}">
                <div class="pica-image-wrapper" style="">
                    <img class="pica-image" style="" src="{{ item['img_api'] }}">
                </div>
            </a>
        </div>
        {% endif %}
        <div class="pica-card-text">
            <a class="pica-link" target="_blank" href="{{ item['link'] }}">
                <h3 style="margin-top: 8px; margin-bottom: 6px; color: black; font-family: -apple-system, BlinkMacSystemFont, avenir, helvetica, ubuntu, roboto, noto, arial, sans-serif; font-weight: 500;" class="">{{ item['title_api']|safe }}</h3>
                <p class="">{% if item['img_api'] == '' %}
                {{ item['desc_user']|safe|truncate(150, False) if item['desc_user'] else item['desc_api']|safe|truncate(150, False) }}<br>
                {% endif %}
                <small style="color: grey;">{{ item['label_user']|safe if item['label_user'] else item['label_api']|safe }}</small></p>
            </a>
        </div>
    </article>
{% endmacro %}

<p><b>WHEN</b>: Ontarians go to the polls on June 7, 2018.</p>
<hr>
</br>
<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/videoseries?list=PL_zQkmt7tH3DqpwwYdZdCaD_mLk2hQa_v' frameborder='0' allowfullscreen></iframe></div>
<hr>
<h2>Area riding profiles:</h2>
<p><a href="/news-story/8614302-riding-profile-hamilton-centre/">Hamilton Centre</a></p>
<p><a href="/news-story/8626730-riding-profile-hamilton-east-stoney-creek/">Hamilton East—Stoney Creek</a></p>
<p><a href="/news-story/8629187-riding-profile-hamilton-mountain/">Hamilton Mountain</a></p>
<p><a href="/news-story/8640951-riding-profile-hamilton-west-ancaster-dundas/">Hamilton West—Ancaster—Dundas</a></p>
<p><a href="/news-story/8638757-riding-profile-flamborough-glanbrook/">Flamborough-Glanbrook</a></p>
<p><a href="/news-story/8624041-here-s-a-look-at-the-burlington-riding-provincial-election-candidates/">Burlington</a></p>
<p><a href="/news-story/8625444-here-s-a-look-at-the-oakville-north-burlington-provincial-election-candidates/">Oakvile North - Burlington</a></p>
<p><a href="/news-story/8624273-here-s-a-look-at-the-milton-riding-provincial-election-candidates/">Milton</a></p>

<hr>
<p><b>MORE INFO</b>: <a class="pica-link b" href="https://www.elections.on.ca/" target="_blank">Elections Ontario</a> | <a class="pica-link b" href="https://www.elections.on.ca/en/voting-in-ontario/electoral-districts.html" target="_blank">Find your riding by postal code</a></p>
{# <hr> #}
<hr>

<section class="pica-cards">
    {%- for item in data['posts']['spec'] -%}
        {{ show_post(item) }}
    {%- endfor %}
</section>
<h2>Halton Region</h2>
<section class="pica-cards">
    {%- for item in data['posts']['halton'] -%}
        {{ show_post(item) }}
    {%- endfor %}
</section>
<h2>Niagara Region</h2>
<section class="pica-cards">
    {%- for item in data['posts']['niagara'] -%}
        {{ show_post(item) }}
    {%- endfor %}
</section>
'''

script_template = '''\
var pica_add = (function() {
    var executed = false;
    return function() {
      if (!executed) {
        if (document.getElementById("pica-style") === null) {
            executed = true;
            var css = '$css',
              head = document.head || document.getElementsByTagName('head')[0],
              style = document.createElement('style');
            style.setAttribute('id', 'pica-style');
            style.type = 'text/css';
            if (style.styleSheet){
              style.styleSheet.cssText = css;
            } else {
              style.appendChild(document.createTextNode(css));
            }
            head.appendChild(style);
          }
        }
    };
})();
pica_add();
var html_string = '$minified';
var matches = document.querySelectorAll('div.pica-results');
for (var i=0; i<matches.length; i++)
    matches[i].innerHTML = html_string;
'''
