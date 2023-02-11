# China domain list for Gost

适用于 Gost 的中国网站屏蔽列表

`gost.yml`
```yaml
services:
  - name: https-proxy
    addr: :443
    bypasses:
      - cnip
      - cndm
      - localip
    handler:
      type: http
      auth:
        username: admin
        password: $(openssl rand -base64 24)
    listener:
      type: tls
      tls:
        certFile: /path/to/cert
        keyFile: /path/to/key
bypasses:
- name: cnip
  file:
    path: cnip.txt
- name: cndm
  file:
    path: cndm.txt
- name: localip
  matchers:
  169.254.0.0/16
  192.168.0.0/16
  172.16.0.0/16
  10.0.0.0/8
```

[^1]:https://github.com/XTLS/Xray-core/discussions/593#discussioncomment-845165
