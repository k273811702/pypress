import tornado.template


def failed_errors(field):
    t = tornado.template.Template("""
    {% if filed.errors %}
        <ul class = "errors">
            {% for error in filed.errors %}
            <li>{{error}}</li>
            <% end %>
        </ul>
    <% end %>
    """)
    return t.generate(field=field)
