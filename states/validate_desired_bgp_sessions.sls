{% for peer in pillar["neighbors"] %}
validate_bgp_session_state_with_{{ peer['peer_ip'] }}:
  loop.until:
    - name: junos.rpc
    - condition: m_ret['rpc_reply']['bgp-information']['bgp-peer']['peer-state'] == 'Established'
    - period: 5
    - timeout: 20
    - m_args:
      - get-bgp-neighbor-information
    - m_kwargs:
        neighbor-address: {{ peer['peer_ip'] }}
{% endfor %}
