#!/usr/bin/env python
# -*- coding: utf-8 -*-
TARGET_URL = 'https://g.alicdn.com/secdev/sufei_data/3.6.11/index.js' #这个是淘宝的index.js文件的
#TARGET_URL = 'https://g.alicdn.com/??kissy/k/1.4.16/seed-min.js,mui/global/3.0.31/global-pc.js,mui/global/3.0.31/global.js,mui/globalmodule/3.0.85/seed.js,mui/btscfg-g/3.0.0/index.js,mui/bucket/3.0.4/index.js,mui/globalmodule/3.0.85/global-mod-pc.js,mui/globalmodule/3.0.85/global-mod.js,mui/global/3.0.31/responsive.js,mui/kissy-polyfill/4.0.16/index.js,zebra-pages/portal-4713/1.2.2/pc/index.js,zebra-pages/portal-4713/1.2.2/seed.js' #这个是天猫的index.js文件的
INJECT_TEXT = 'Object.defineProperties(navigator,{webdriver:{get:() => false}});' #js执行文件

def response(flow):
        if flow.request.url.startswith(TARGET_URL):
            flow.response.text = INJECT_TEXT + flow.response.text
            print('注入成功')
        if 'um.js' in flow.request.url or '115.js' in flow.request.url:
            # 屏蔽selenium检测
            flow.response.text = flow.response.text + INJECT_TEXT
