
<ul>
  {% for item in options %}
  <li>{{item['name']}}</li>
  {% endfor%}
</ul>



<ul class="teachers">
  {% for teacher in teachers %}
  <li><h2>{{teacher['name']}}</h2>
    <ul class="courses">
      {% for course in teacher['courses']%}
      <li>{{course}}</li>
      {% endfor %}
    </ul>
  </li>
  {% endfor %}
</ul>