{% extends "basic.tpl" %}

{% block codecell %}
  {% if "red-border" in cell.metadata.get('tags', []) %}
  <div style="border:thin solid red">
    {{ super() }}
  </div>
  {% elif "display-none" in cell.metadata.get('tags', []) %}
  <div style="display:none">
    {{ super() }}
  </div>
  {% else %}
  {{ super() }}
  {% endif %}
{% endblock codecell %}

{% block input_group %}
  {% if "toggle-code" in cell.metadata.get('tags', []) %}
  <button class="toggle-button">Toggle Code</button>
  <div style="display: none">
    {{ super() }}
  </div>
  {% else %}
  {{ super() }}
  {% endif %}
{% endblock %}