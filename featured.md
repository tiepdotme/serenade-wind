---
layout: default
title: Featured Post
permalink: /featured/
---
    {%- for entry in site.posts -%}
      {%- if entry.featured == true -%}
        {%- assign page = entry -%}
      {%- endif -%}
    {%- endfor -%}
{% include post-layout.html%}