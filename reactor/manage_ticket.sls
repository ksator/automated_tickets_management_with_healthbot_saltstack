{% if data['data'] is defined %}
{% set d = data['data'] %}
{% else %}
{% set d = data %}
{% endif %}
{% set body_json = d['body']|load_json %}
{% set message = body_json['message'] %}

create_a_new_ticket_or_update_the_existing_one:
    runner.request_tracker.create_ticket:
        - args:
            subject: "device {{ message }}"
            text: "{{ message }}"
