# China domain list for Gost

适用于 Gost 的中国网站屏蔽列表

使用 [Domain list community](https://github.com/v2fly/domain-list-community) 和 [chnroutes2](https://github.com/misakaio/chnroutes2)

```shell
mkdir /etc/gost && cd /etc/gost
# chown gostuser: .
wget https://raw.githubusercontent.com/wsm25/cn-domain-list-gost/main/cndm.txt
wget https://raw.githubusercontent.com/wsm25/cn-domain-list-gost/main/cnip.txt
wget https://raw.githubusercontent.com/wsm25/cn-domain-list-gost/main/gost.yml
gost
```

[^1]:https://github.com/XTLS/Xray-core/discussions/593#discussioncomment-845165
