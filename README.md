# mailx

Role to install mailx.

## Requirements

None

## Role Variables

* `email`: Dictionary with the information of the configuration.
  * `server`: endpoint of the server (Example: `smtp://disroot.org:587`).
  * `user`: user to authenticate to the SMTP server.
  * `password`: password to authenticate to the SMTP server.
  * `from`: email address that will appear in the FROM of the email.

## Dependencies

## Example playbook

```yaml
- hosts: all
  roles:
    - mailx
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/).

```bash
molecule test
```

## License

GPLv2

## Author Information
Lyz (lyz@riseup.net)
