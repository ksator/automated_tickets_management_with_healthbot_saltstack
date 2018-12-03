configure_bgp:
    junos.install_config:
        - name: salt://bgp.conf
        - timeout: 20
        - replace: True
        - overwrite: False
        - comment: "configured with SaltStack using the model bgp"

