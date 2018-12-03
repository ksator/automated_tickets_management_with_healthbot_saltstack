configure_extension_service:
    junos.install_config:
        - name: salt://extension_service.conf
        - timeout: 20
        - replace: False
        - overwrite: False
        - comment: "configured with SaltStack using the model extension_service"


