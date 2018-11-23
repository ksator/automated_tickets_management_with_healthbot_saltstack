{% set body_json = data['body']|load_json %}

{% set message = body_json['message'] %}
{% set device = body_json['device-id'] %}
{% set rule = body_json['rule'] %}
{% set group = body_json['group'] %}
{% set trigger = body_json['trigger'] %}
{% set instance = body_json['keys']['instance-id'] %}

create_a_new_ticket_or_update_the_existing_one:
    runner.request_tracker.create_ticket:
        - args:
            subject: "rule {{ rule }} - trigger {{ trigger }} -  device-group {{ group }} - instance {{ instance }}"
            text: "device {{ device }} - message {{ message }}"

