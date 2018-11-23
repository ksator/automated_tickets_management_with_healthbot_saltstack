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
            subject: "healthbot rule {{ rule }} - trigger {{ trigger }} - device-group {{ group }} - device {{ device }} - instance {{ instance }}"
            text: "message {{ message }}"

show_commands_output_collection:
    local.state.apply:
        - tgt: "{{ device }}"
        - arg:
            - collect_data_locally_and_push_to_master
            
attach_files_to_a_ticket:
    runner.request_tracker.attach_files_to_ticket:
        - args:
            subject: "healthbot rule {{ rule }} - trigger {{ trigger }} - device-group {{ group }} - device {{ device }} - instance {{ instance }}"
            device_directory: "{{ device }}"
        - require:
            - show_commands_output_collection
            - create_a_new_ticket_or_update_the_existing_one


