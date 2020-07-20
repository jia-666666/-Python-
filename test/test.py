html="""
<HTML class="ks-webkit537 ks-webkit ks-chrome80 ks-chrome no-touch"><head><script src="//top-tmm.taobao.com/login_api.do?0.2583684022794428" async=""/><script charset="utf-8" src="https://g.alicdn.com/tm/list/2.25.17/??shortcut.js?t=20130804.js" async=""/><script type="text/javascript" async="" src="https://g.alicdn.com/secdev/entry/index.js?t=220179" id="aplus-sufei"/><script charset="utf-8" src="https://g.alicdn.com/mui/??iconfont/1.0.6/fontloader.js?t=20130804.js" async=""/><script>/*! 2020-03-17 20:01:01 v8.13.5 */
!function(e){function i(n){if(o[n])return o[n].exports;var r=o[n]={exports:{},id:n,loaded:!1};return e[n].call(r.exports,r,r.exports,i),r.loaded=!0,r.exports}var o={};return i.m=e,i.c=o,i.p="",i(0)}([function(e,i){"use strict";var o=window,n=document;!function(){var e=2,r="ali_analytics";if(o[r]&amp;&amp;o[r].ua&amp;&amp;e&lt;=o[r].ua.version)return void(i.info=o[r].ua);var t,a,d,s,c,u,h,l,m,b,f,v,p,w,g,x,z,O=o.navigator,k=O.appVersion,T=O&amp;&amp;O.userAgent||"",y=function(e){var i=0;return parseFloat(e.replace(/\./g,function(){return 0===i++?".":""}))},_=function(e,i){var o,n;i[o="trident"]=.1,(n=e.match(/Trident\/([\d.]*)/))&amp;&amp;n[1]&amp;&amp;(i[o]=y(n[1])),i.core=o},N=function(e){var i,o;return(i=e.match(/MSIE ([^;]*)|Trident.*; rv(?:\s|:)?([0-9.]+)/))&amp;&amp;(o=i[1]||i[2])?y(o):0},P=function(e){return e||"other"},M=function(e){function i(){for(var i=[["Windows NT 5.1","winXP"],["Windows NT 6.1","win7"],["Windows NT 6.0","winVista"],["Windows NT 6.2","win8"],["Windows NT 10.0","win10"],["iPad","ios"],["iPhone;","ios"],["iPod","ios"],["Macintosh","mac"],["Android","android"],["Ubuntu","ubuntu"],["Linux","linux"],["Windows NT 5.2","win2003"],["Windows NT 5.0","win2000"],["Windows","winOther"],["rhino","rhino"]],o=0,n=i.length;o&lt;n;++o)if(e.indexOf(i[o][0])!==-1)return i[o][1];return"other"}function r(e,i,n,r){var t,a=o.navigator.mimeTypes;try{for(t in a)if(a.hasOwnProperty(t)&amp;&amp;a[t][e]==i){if(void 0!==n&amp;&amp;r.test(a[t][n]))return!0;if(void 0===n)return!0}return!1}catch(e){return!1}}var t,a,d,s,c,u,h,l="",m=l,b=l,f=[6,9],v="{{version}}",p="&lt;!--[if IE "+v+"]&gt;&lt;s&gt;&lt;/s&gt;&lt;![endif]--&gt;",w=n&amp;&amp;n.createElement("div"),g=[],x={webkit:void 0,edge:void 0,trident:void 0,gecko:void 0,presto:void 0,chrome:void 0,safari:void 0,firefox:void 0,ie:void 0,ieMode:void 0,opera:void 0,mobile:void 0,core:void 0,shell:void 0,phantomjs:void 0,os:void 0,ipad:void 0,iphone:void 0,ipod:void 0,ios:void 0,android:void 0,nodejs:void 0,extraName:void 0,extraVersion:void 0};if(w&amp;&amp;w.getElementsByTagName&amp;&amp;(w.innerHTML=p.replace(v,""),g=w.getElementsByTagName("s")),g.length&gt;0){for(_(e,x),s=f[0],c=f[1];s&lt;=c;s++)if(w.innerHTML=p.replace(v,s),g.length&gt;0){x[b="ie"]=s;break}!x.ie&amp;&amp;(d=N(e))&amp;&amp;(x[b="ie"]=d)}else((a=e.match(/AppleWebKit\/*\s*([\d.]*)/i))||(a=e.match(/Safari\/([\d.]*)/)))&amp;&amp;a[1]?(x[m="webkit"]=y(a[1]),(a=e.match(/OPR\/(\d+\.\d+)/))&amp;&amp;a[1]?x[b="opera"]=y(a[1]):(a=e.match(/Chrome\/([\d.]*)/))&amp;&amp;a[1]?x[b="chrome"]=y(a[1]):(a=e.match(/\/([\d.]*) Safari/))&amp;&amp;a[1]?x[b="safari"]=y(a[1]):x.safari=x.webkit,(a=e.match(/Edge\/([\d.]*)/))&amp;&amp;a[1]&amp;&amp;(m=b="edge",x[m]=y(a[1])),/ Mobile\//.test(e)&amp;&amp;e.match(/iPad|iPod|iPhone/)?(x.mobile="apple",a=e.match(/OS ([^\s]*)/),a&amp;&amp;a[1]&amp;&amp;(x.ios=y(a[1].replace("_","."))),t="ios",a=e.match(/iPad|iPod|iPhone/),a&amp;&amp;a[0]&amp;&amp;(x[a[0].toLowerCase()]=x.ios)):/ Android/i.test(e)?(/Mobile/.test(e)&amp;&amp;(t=x.mobile="android"),a=e.match(/Android ([^\s]*);/),a&amp;&amp;a[1]&amp;&amp;(x.android=y(a[1]))):(a=e.match(/NokiaN[^\/]*|Android \d\.\d|webOS\/\d\.\d/))&amp;&amp;(x.mobile=a[0].toLowerCase()),(a=e.match(/PhantomJS\/([^\s]*)/))&amp;&amp;a[1]&amp;&amp;(x.phantomjs=y(a[1]))):(a=e.match(/Presto\/([\d.]*)/))&amp;&amp;a[1]?(x[m="presto"]=y(a[1]),(a=e.match(/Opera\/([\d.]*)/))&amp;&amp;a[1]&amp;&amp;(x[b="opera"]=y(a[1]),(a=e.match(/Opera\/.* Version\/([\d.]*)/))&amp;&amp;a[1]&amp;&amp;(x[b]=y(a[1])),(a=e.match(/Opera Mini[^;]*/))&amp;&amp;a?x.mobile=a[0].toLowerCase():(a=e.match(/Opera Mobi[^;]*/))&amp;&amp;a&amp;&amp;(x.mobile=a[0]))):(d=N(e))?(x[b="ie"]=d,_(e,x)):(a=e.match(/Gecko/))&amp;&amp;(x[m="gecko"]=.1,(a=e.match(/rv:([\d.]*)/))&amp;&amp;a[1]&amp;&amp;(x[m]=y(a[1]),/Mobile|Tablet/.test(e)&amp;&amp;(x.mobile="firefox")),(a=e.match(/Firefox\/([\d.]*)/))&amp;&amp;a[1]&amp;&amp;(x[b="firefox"]=y(a[1])));t||(t=i());var z,O,T;if(!r("type","application/vnd.chromium.remoting-viewer")){z="scoped"in n.createElement("style"),T="v8Locale"in o;try{O=o.external||void 0}catch(e){}if(a=e.match(/360SE/))u="360";else if((a=e.match(/SE\s([\d.]*)/))||O&amp;&amp;"SEVersion"in O)u="sougou",h=y(a[1])||.1;else if((a=e.match(/Maxthon(?:\/)+([\d.]*)/))&amp;&amp;O){u="maxthon";try{h=y(O.max_version||a[1])}catch(e){h=.1}}else z&amp;&amp;T?u="360se":z||T||!/Gecko\)\s+Chrome/.test(k)||x.opera||x.edge||(u="360ee")}(a=e.match(/TencentTraveler\s([\d.]*)|QQBrowser\/([\d.]*)/))?(u="tt",h=y(a[2])||.1):(a=e.match(/LBBROWSER/))||O&amp;&amp;"LiebaoGetVersion"in O?u="liebao":(a=e.match(/TheWorld/))?(u="theworld",h=3):(a=e.match(/TaoBrowser\/([\d.]*)/))?(u="taobao",h=y(a[1])||.1):(a=e.match(/UCBrowser\/([\d.]*)/))&amp;&amp;(u="uc",h=y(a[1])||.1),x.os=t,x.core=x.core||m,x.shell=b,x.ieMode=x.ie&amp;&amp;n.documentMode||x.ie,x.extraName=u,x.extraVersion=h;var P=o.screen.width,M=o.screen.height;return x.resolution=P+"x"+M,x},S=function(e){function i(e){return Object.prototype.toString.call(e)}function o(e,o,n){if("[object Function]"==i(o)&amp;&amp;(o=o(n)),!o)return null;var r={name:e,version:""},t=i(o);if(o===!0)return r;if("[object String]"===t){if(n.indexOf(o)!==-1)return r}else if(o.exec){var a=o.exec(n);if(a)return a.length&gt;=2&amp;&amp;a[1]?r.version=a[1].replace(/_/g,"."):r.version="",r}}var n={name:"other",version:""};e=(e||"").toLowerCase();for(var r=[["nokia",function(e){return e.indexOf("nokia ")!==-1?/\bnokia ([0-9]+)?/:/\bnokia([a-z0-9]+)?/}],["samsung",function(e){return e.indexOf("samsung")!==-1?/\bsamsung(?:[ \-](?:sgh|gt|sm))?-([a-z0-9]+)/:/\b(?:sgh|sch|gt|sm)-([a-z0-9]+)/}],["wp",function(e){return e.indexOf("windows phone ")!==-1||e.indexOf("xblwp")!==-1||e.indexOf("zunewp")!==-1||e.indexOf("windows ce")!==-1}],["pc","windows"],["ipad","ipad"],["ipod","ipod"],["iphone",/\biphone\b|\biph(\d)/],["mac","macintosh"],["mi",/\bmi[ \-]?([a-z0-9 ]+(?= build|\)))/],["hongmi",/\bhm[ \-]?([a-z0-9]+)/],["aliyun",/\baliyunos\b(?:[\-](\d+))?/],["meizu",function(e){return e.indexOf("meizu")&gt;=0?/\bmeizu[\/ ]([a-z0-9]+)\b/:/\bm([0-9x]{1,3})\b/}],["nexus",/\bnexus ([0-9s.]+)/],["huawei",function(e){var i=/\bmediapad (.+?)(?= build\/huaweimediapad\b)/;return e.indexOf("huawei-huawei")!==-1?/\bhuawei\-huawei\-([a-z0-9\-]+)/:i.test(e)?i:/\bhuawei[ _\-]?([a-z0-9]+)/}],["lenovo",function(e){return e.indexOf("lenovo-lenovo")!==-1?/\blenovo\-lenovo[ \-]([a-z0-9]+)/:/\blenovo[ \-]?([a-z0-9]+)/}],["zte",function(e){return/\bzte\-[tu]/.test(e)?/\bzte-[tu][ _\-]?([a-su-z0-9\+]+)/:/\bzte[ _\-]?([a-su-z0-9\+]+)/}],["vivo",/\bvivo(?: ([a-z0-9]+))?/],["htc",function(e){return/\bhtc[a-z0-9 _\-]+(?= build\b)/.test(e)?/\bhtc[ _\-]?([a-z0-9 ]+(?= build))/:/\bhtc[ _\-]?([a-z0-9 ]+)/}],["oppo",/\boppo[_]([a-z0-9]+)/],["konka",/\bkonka[_\-]([a-z0-9]+)/],["sonyericsson",/\bmt([a-z0-9]+)/],["coolpad",/\bcoolpad[_ ]?([a-z0-9]+)/],["lg",/\blg[\-]([a-z0-9]+)/],["android",/\bandroid\b|\badr\b/],["blackberry",function(e){return e.indexOf("blackberry")&gt;=0?/\bblackberry\s?(\d+)/:"bb10"}]],t=0;t&lt;r.length;t++){var a=r[t][0],d=r[t][1],s=o(a,d,e);if(s){n=s;break}}return n},E=1;try{t=M(T),a=S(T),d=t.os,s=t.shell,c=t.core,u=t.resolution,h=t.extraName,l=t.extraVersion,m=a.name,b=a.version,v=d?d+(t[d]?t[d]:""):"",p=s?s+parseInt(t[s]):"",w=c,g=u,x=h?h+(l?parseInt(l):""):"",z=m+b}catch(e){}f={p:E,o:P(v),b:P(p),w:P(w),s:g,mx:x,ism:z},o[r]||(o[r]={}),o[r].ua||(o[r].ua={}),o.goldlog||(o.goldlog={}),i.info=o[r].ua=goldlog._aplus_client={version:e,ua_info:f}}()}]);/*! 2017-10-31 20:15:15 v0.2.4 */
!function(t){function e(o){if(n[o])return n[o].exports;var i=n[o]={exports:{},id:o,loaded:!1};return t[o].call(i.exports,i,i.exports,e),i.loaded=!0,i.exports}var n={};return e.m=t,e.c=n,e.p="",e(0)}([function(t,e,n){"use strict";!function(){var t=window.goldlog||(window.goldlog={});t._aplus_cplugin_utilkit||(t._aplus_cplugin_utilkit={status:"init"},n(1).init(t),t._aplus_cplugin_utilkit.status="complete")}()},function(t,e,n){"use strict";var o=n(2),i=n(4);e.init=function(t){t.setCookie=o.setCookie,t.getCookie=o.getCookie,t.on=i.on}},function(t,e,n){"use strict";var o=document,i=n(3),a=function(t){var e=new RegExp("(?:^|;)\\s*"+t+"=([^;]+)"),n=o.cookie.match(e);return n?n[1]:""};e.getCookie=a;var r=function(t,e,n){n||(n={});var i=new Date;return n.expires&amp;&amp;("number"==typeof n.expires||n.expires.toUTCString)?("number"==typeof n.expires?i.setTime(i.getTime()+24*n.expires*60*60*1e3):i=n.expires,e+="; expires="+i.toUTCString()):"session"!==n.expires&amp;&amp;(i.setTime(i.getTime()+63072e7),e+="; expires="+i.toUTCString()),e+="; path="+(n.path?n.path:"/"),e+="; domain="+n.domain,o.cookie=t+"="+e,a(t)};e.setCookie=function(t,e,n){try{if(n||(n={}),n.domain)r(t,e,n);else for(var o=i.getDomains(),a=0;a&lt;o.length;)n.domain=o[a],r(t,e,n)?a=o.length:a++}catch(t){}}},function(t,e){"use strict";e.getDomains=function(){var t=[];try{for(var e=location.hostname,n=e.split("."),o=2;o&lt;=n.length;)t.push(n.slice(n.length-o).join(".")),o++}catch(t){}return t}},function(t,e){"use strict";var n=window,o=document,i=!!o.attachEvent,a="attachEvent",r="addEventListener",c=i?a:r,u=function(t,e){var n=goldlog._$||{},o=n.meta_info||{},i=o.aplus_ctap||{};if(i&amp;&amp;"function"==typeof i.on)i.on(t,e);else{var a="ontouchend"in document.createElement("div"),r=a?"touchstart":"mousedown";s(t,r,e)}},s=function(t,e,o){return"tap"===e?void u(t,o):void t[c]((i?"on":"")+e,function(t){t=t||n.event;var e=t.target||t.srcElement;"function"==typeof o&amp;&amp;o(t,e)},!1)};e.on=s;var d=function(t){try{o.documentElement.doScroll("left")}catch(e){return void setTimeout(function(){d(t)},1)}t()},l=function(t){var e=0,n=function(){0===e&amp;&amp;t(),e++};"complete"===o.readyState&amp;&amp;n();var i;if(o.addEventListener)i=function(){o.removeEventListener("DOMContentLoaded",i,!1),n()},o.addEventListener("DOMContentLoaded",i,!1),window.addEventListener("load",n,!1);else if(o.attachEvent){i=function(){"complete"===o.readyState&amp;&amp;(o.detachEvent("onreadystatechange",i),n())},o.attachEvent("onreadystatechange",i),window.attachEvent("onload",n);var a=!1;try{a=null===window.frameElement}catch(t){}o.documentElement.doScroll&amp;&amp;a&amp;&amp;d(n)}};e.DOMReady=function(t){l(t)},e.onload=function(t){"complete"===o.readyState?t():s(n,"load",t)}}]);!function(o){function t(r){if(e[r])return e[r].exports;var a=e[r]={exports:{},id:r,loaded:!1};return o[r].call(a.exports,a,a.exports,t),a.loaded=!0,a.exports}var e={};return t.m=o,t.c=e,t.p="",t(0)}([function(o,t,e){"use strict";!function(){var o=window.goldlog||(window.goldlog={});o._aplus_cplugin_m||(o._aplus_cplugin_m=e(1).run())}()},function(o,t,e){"use strict";var r=e(2),a=e(3),n=e(4),s=navigator.sendBeacon?"post":"get";e(5).run(),t.run=function(){return{status:"complete",do_tracker_jserror:function(o){try{var t=new n({logkey:o?o.logkey:"",ratio:o&amp;&amp;"number"==typeof o.ratio&amp;&amp;o.ratio&gt;0?o.ratio:r.jsErrorRecordRatio}),e=["Message: "+o.message,"Error object: "+o.error,"Url: "+location.href].join(" - "),c=goldlog.spm_ab||[],i=location.hostname+location.pathname;t.run({code:110,page:i,msg:"record_jserror_by"+s+"_"+o.message,spm_a:c[0],spm_b:c[1],c1:e,c2:o.filename,c3:location.protocol+"//"+i,c4:goldlog.pvid||"",c5:o.logid||""})}catch(o){a.logger({msg:o})}},do_tracker_lostpv:function(o){var t=!1;try{if(o&amp;&amp;o.page){var e=o.spm_ab?o.spm_ab.split("."):[],c="record_lostpv_by"+s+"_"+o.msg,i=new n({ratio:o.ratio||r.lostPvRecordRatio});i.run({code:102,page:o.page,msg:c,spm_a:e[0],spm_b:e[1],c1:o.duration,c2:o.page_url}),t=!0}}catch(o){a.logger({msg:o})}return t},do_tracker_obsolete_inter:function(o){var t=!1;try{if(o&amp;&amp;o.page){var e=o.spm_ab?o.spm_ab.split("."):[],c="record_obsolete interface be called by"+s,i=new n({ratio:o.ratio||r.obsoleteInterRecordRatio});i.run({code:109,page:o.page,msg:c,spm_a:e[0],spm_b:e[1],c1:o.interface_name,c2:o.interface_params},1),t=!0}}catch(o){a.logger({msg:o})}return t},do_tracker_browser_support:function(o){var t=!1;try{if(o&amp;&amp;o.page){var e=o.spm_ab?o.spm_ab.split("."):[],c=new n({ratio:o.ratio||r.browserSupportRatio}),i=goldlog._aplus_client||{},l=i.ua_info||{};c.run({code:111,page:o.page,msg:o.msg+"_by"+s,spm_a:e[0],spm_b:e[1],c1:[l.o,l.b,l.w].join("_"),c2:o.etag||"",c3:o.cna||""}),t=!0}}catch(o){a.logger({msg:o})}return t},do_tracker_common_analysis:function(o){var t=!1;try{if(o&amp;&amp;o.page){var e=o.spm_ab?o.spm_ab.split("."):[],c=new n({ratio:o.ratio||r.browserSupportRatio}),i=goldlog._aplus_client||{},l=i.ua_info||{};c.run({code:113,page:o.page,msg:o.msg+"_by"+s,spm_a:e[0],spm_b:e[1],c1:[l.o,l.b,l.w].join("_"),c2:o.init_time||"",c3:o.wspv_time||0,c4:o.load_time||0,c5:o.channel_type}),t=!0}}catch(o){a.logger({msg:o})}return t}}}},function(o,t){"use strict";t.lostPvRecordRatio="0.01",t.obsoleteInterRecordRatio="0.001",t.jsErrorRecordRatio="0.001",t.browserSupportRatio="0.001",t.goldlogQueueRatio="0.01"},function(o,t){"use strict";var e=function(o){var t=o.level||"warn";window.console&amp;&amp;window.console[t]&amp;&amp;window.console[t](o.msg)};t.logger=e,t.assign=function(o,t){if("function"!=typeof Object.assign){var e=function(o){if(null===o)throw new TypeError("Cannot convert undefined or null to object");for(var t=Object(o),e=1;e&lt;arguments.length;e++){var r=arguments[e];if(null!==r)for(var a in r)Object.prototype.hasOwnProperty.call(r,a)&amp;&amp;(t[a]=r[a])}return t};return e(o,t)}return Object.assign({},o,t)},t.makeCacheNum=function(){return Math.floor(268435456*Math.random()).toString(16)},t.obj2param=function(o){var t,e,r=[];for(t in o)o.hasOwnProperty(t)&amp;&amp;(e=""+o[t],r.push(t+"="+encodeURIComponent(e)));return r.join("&amp;")}},function(o,t,e){var r=e(3),a={ratio:1,logkey:"fsp.1.1",gmkey:"",chksum:"H46747615"},n=function(o){o&amp;&amp;"object"==typeof o||(o=a),this.opts=o,this.opts.ratio=o.ratio||a.ratio,this.opts.logkey=o.logkey||a.logkey,this.opts.gmkey=o.gmkey||a.gmkey,this.opts.chksum=o.chksum||a.chksum},s=n.prototype;s.getRandom=function(){return Math.floor(1e3*Math.random())+1},s.run=function(o,t){var e,a,n={pid:"aplus",code:101,msg:"异常内容"},s="";try{var c=window.goldlog||{},i=c._$||{},l=i.meta_info||{},g=parseFloat(l["aplus-tracker-rate"]);if(e=this.opts||{},"number"==typeof g&amp;&amp;g+""!="NaN"||(g=e.ratio),a=this.getRandom(),t||a&lt;=1e3*g){s="//gm.mmstat.com/"+e.logkey,o.rel=i.script_name+"@"+c.lver,o.type=o.code,o.uid=encodeURIComponent(c.getCookie("cna")),o=r.assign(n,o);var u=r.obj2param(o);c.tracker=c.send(s,{cache:r.makeCacheNum(),gokey:u,logtype:"2"},"POST")}}catch(o){r.logger({msg:"tracker.run() exec error: "+o})}},o.exports=n},function(o,t,e){"use strict";var r=e(6),a=function(o){var t=window.goldlog||{},e=t._$=t._$||{},r=t.spm_ab?t.spm_ab.join("."):"0.0",a=e.send_pv_count||0;if(a&lt;1&amp;&amp;navigator&amp;&amp;navigator.sendBeacon){var n=window.goldlog_queue||(window.goldlog_queue=[]),s=location.hostname+location.pathname;n.push({action:["goldlog","_aplus_cplugin_m","do_tracker_lostpv"].join("."),arguments:[{page:s,page_url:location.protocol+"//"+s,duration:o,spm_ab:r,msg:"dom_state="+document.readyState}]})}};t.run=function(){var o=new Date;r.on(window,"beforeunload",function(){var t=new Date,e=t.getTime()-o.getTime();a(e)})}},function(o,t){"use strict";var e=self,r=e.document,a=!!r.attachEvent,n="attachEvent",s="addEventListener",c=a?n:s;t.getIframeUrl=function(o){var t,e="//g.alicdn.com";return t=goldlog&amp;&amp;"function"==typeof goldlog.getCdnPath?goldlog.getCdnPath()||e:e,(o||"https")+":"+t+"/alilog/aplus_cplugin/@@APLUS_CPLUGIN_VER/ls.HTML?t=@@_VERSION_"},t.on=function(o,t,r){o[c]((a?"on":"")+t,function(o){o=o||e.event;var t=o.target||o.srcElement;"function"==typeof r&amp;&amp;r(o,t)},!1)},t.checkLs=function(){var o;try{window.localStorage&amp;&amp;(localStorage.setItem("test_log_cna","1"),"1"===localStorage.getItem("test_log_cna")&amp;&amp;(localStorage.removeItem("test_log_cna"),o=!0))}catch(t){o=!1}return o},t.tracker_iframe_status=function(o,t){var e=window.goldlog_queue||(window.goldlog_queue=[]),r=goldlog.spm_ab?goldlog.spm_ab.join("."):"",a="createIframe_"+t.status+"_id="+o;t.msg&amp;&amp;(a+="_"+t.msg),e.push({action:"goldlog._aplus_cplugin_m.do_tracker_browser_support",arguments:[{page:location.hostname+location.pathname,msg:a,browser_attr:navigator.userAgent,spm_ab:r,cna:t.duration||"",ratio:1}]})},t.tracker_ls_failed=function(){var o=window.goldlog_queue||(window.goldlog_queue=[]),t=goldlog.spm_ab?goldlog.spm_ab.join("."):"";o.push({action:"goldlog._aplus_cplugin_m.do_tracker_browser_support",arguments:[{page:location.hostname+location.pathname,msg:"donot support localStorage",browser_attr:navigator.userAgent,spm_ab:t}]})},t.processMsgData=function(o){var t={};try{var e="{}";e="TextEncoder"in window&amp;&amp;"object"==typeof o?new window.TextDecoder("utf-8").decode(o):o,t=JSON.parse(e)}catch(o){t={}}return t},t.do_pub_fn=function(o,t){var e=window.goldlog_queue||(window.goldlog_queue=[]);e.push({action:"goldlog.aplus_pubsub.publish",arguments:[o,t]}),e.push({action:"goldlog.aplus_pubsub.cachePubs",arguments:[o,t]})}}]);/*! 2020-03-17 20:01:01 v8.13.5 */
!function(t){function e(r){if(n[r])return n[r].exports;var o=n[r]={exports:{},id:r,loaded:!1};return t[r].call(o.exports,o,o.exports,e),o.loaded=!0,o.exports}var n={};return e.m=t,e.c=n,e.p="",e(0)}([function(t,e,n){"use strict";!function(){var t,e=window;try{var r="function";t=typeof e.WebSocket===r&amp;&amp;typeof e.WebSocket.prototype.send===r}catch(t){}if(t){var o=e.goldlog||(e.goldlog={});if(o._aplus_cplugin_ws)return;o._aplus_cplugin_ws=!0;var a=n(1),s=a.create();s.run()}}()},function(t,e,n){"use strict";var r=window,o=n(2),a=n(3),s=n(13),i=n(16),u=n(6),c=n(8),l=n(17),f=n(18),h=n(20),p=n(21),g=n(22);t.exports=o.extend({wsHandler:"",lsCnaKey:"APLUS_CNA",timeoutToHttp:3e3,domain:"log.mmstat.com",retryTimesKey:"aplusx_retry_times",maxRetryTimesPerHour:3,retryTimes:0,pageLoadDateHour:"",getDateHour:function(){return l.getFormatDate()+(new Date).getHours()},getRandom:function(t,e){return t+Math.floor(Math.random()*(e-t+1))},getRetryTimes:function(){var t=0,e=c.get(this.retryTimesKey);if(e){var n=e.split("-");2===n.length&amp;&amp;n[0]===this.getDateHour()&amp;&amp;(t=parseInt(n[1]))}return t},setRetryTimes:function(t){c.set(this.retryTimesKey,this.getDateHour()+"-"+t)},doSetRetryTimes:function(){this.retryTimes&lt;this.maxRetryTimesPerHour?this.setRetryTimes(++this.retryTimes):this.retryTimes&gt;=this.maxRetryTimesPerHour&amp;&amp;this.pageLoadDateHour!==this.getDateHour()&amp;&amp;(this.retryTimes=0,this.setRetryTimes(++this.retryTimes))},cheatCallback:function(t,e){c.set(t.toUpperCase(),e)},newSend:function(t,e,n,r){var o=this;i(t,function(e,n){"number"!=typeof n&amp;&amp;"boolean"!=typeof n||(t[e]=n+"")});var a=c.get("APLUS_SN"),s=c.get("APLUS_SY");try{a&amp;&amp;(t.aplus_sn=a),s&amp;&amp;(t.aplus_sy=s),t.ua=navigator.userAgent,t.lang=navigator.language}catch(t){}this.wsHandler.send({id:"id"+o.getRandom(1,1e8),startTime:(new Date).getTime(),type:e,msg:{postData:JSON.stringify(t),url:n},method:r})},getPvPostData:function(t){var e,n=t.is_single,r=t.where_to_sendlog_ut.aplusToUT.toutflag,o=t.where_to_sendpv.url,s="//log.mmstat.com/o.gif";if("toUT2"===r&amp;&amp;!n||"toUT"===r&amp;&amp;!n||"toUT2"!==r&amp;&amp;"toUT"!==r){s=t.where_to_sendpv.url,e=t.what_to_sendpv.pvdata;var i=o.match(/\/\w+.gif/),u=i?i[0]:"/v.gif",c=a.arr2param(e),l=c.indexOf("&amp;aplus&amp;")&gt;-1?"&amp;aplus&amp;":"&amp;aplus=&amp;",f=c.split(l),h=a.param2obj(f[0]);return{postData:a.assign(h,{logkey:u,url:location.href,gokey:f[1].replace(/&amp;aws=1/,"")}),mmurl:s}}},pv_callback:function(t){try{var e=this.getPvPostData(t);e&amp;&amp;this.newSend(e.postData,"pv",e.mmurl)}catch(t){g.catchException("pv_callback",t)}},getHjljPostData:function(t){var e=t.is_single,n={},r=t.where_to_sendlog_ut.aplusToUT.toutflag,o="";if("toUT2"===r&amp;&amp;!e||"toUT"===r&amp;&amp;!e)o=t.where_to_hjlj.url,n=t.what_to_hjlj.logdata,n.logkey=n.logkey||"";else{if("toUT2"===r||"toUT"===r)return;o=t.where_to_hjlj.url,n=t.what_to_hjlj.logdata,n.logkey=t.userdata?t.userdata.logkey:""}return n.url=location.href,n.gokey&amp;&amp;(n.gokey=n.gokey.replace(/&amp;aws=1/,"")),{postData:n,mmurl:o}},hjlj_callback:function(t){try{var e=this.getHjljPostData(t);e&amp;&amp;this.newSend(e.postData,"goldlog",e.mmurl,t.method)}catch(t){g.catchException("hjlj_callback",t)}},getCnaData:function(){var t={params:[]},e=u.getLsCna(this.lsCnaKey),n=f.getCookie("cna");return t.cna=e||n,e&amp;&amp;!n&amp;&amp;t.params.push("lstag=1"),t},cnaCallback:function(t,e){var n=u.getLsCna(this.lsCnaKey),r=f.getCookie("cna");n===r&amp;&amp;n===e&amp;&amp;r===e||(u.setLsCna(this.lsCnaKey,l.getFormatDate(),e),f.setCookie(t,e,{SameSite:"none"}))},watchWSStatus:function(t){var e=this;this.wsHandler.subscribe("APLUS_WS_OPEN",function(){t===e.maxRetryTimesPerHour&amp;&amp;(e.retryTimes=0,e.setRetryTimes(e.retryTimes))}),this.wsHandler.subscribe("APLUS_WS_ERROR",function(){e.doSetRetryTimes(),e.msgQueueToHttpRequest()}),this.wsHandler.subscribe("APLUS_WS_EXCEPTION",function(){e.doSetRetryTimes(),e.msgQueueToHttpRequest()}),this.wsHandler.subscribe("APLUS_WS_CLOSE",function(){e.msgQueueToHttpRequest()})},startWebSocket:function(){var t=this,e=this.getCnaData();this.wsHandler=p.create({cna:e.cna,params:e.params,createTime:(new Date).getTime()}),this.wsHandler.startWS(),this.watchWSStatus(this.getRetryTimes()),this.wsHandler.subscribe("APLUS_WS_SERVER_MSG",function(e){if(e){var n=e.indexOf(":"),r=e.substr(0,n),o=e.substr(n+1);switch(r){case"cna":t.cnaCallback(r,o);break;case"aplus_sn":case"aplus_sy":t.cheatCallback(r,o);break;default:var a={};a[r]=o,goldlog.send("//"+t.domain+"/s",a)}}})},subscribeLogs:function(t,e){h.pushIntoGoldlogQueue("goldlog.aplus_pubsub.subscribe",[t,function(t){"complete"===t.status&amp;&amp;e(t)}])},enableSendByWS:function(t){var e=goldlog.getMetaInfo("aplus-channel"),n=["WS","WS-ONLY"],r=n.indexOf(goldlog.aplusChannel)&gt;-1||n.indexOf(e)&gt;-1||n.indexOf(t)&gt;-1;return r},watchLOG:function(){var t=this;t.subscribeLogs("mw_change_pv",function(e){var n=t.enableSendByWS(e.method);if(n===!0)if(t.retryTimes&gt;=t.maxRetryTimesPerHour){var r=a.arr2obj(e.what_to_sendpv.pvdata);delete r.aws,r._j=1,goldlog.send(e.where_to_sendpv.url,r)}else t.pv_callback(e)}),t.subscribeLogs("mw_change_hjlj",function(e){var n="POST"===e.method;if(t.enableSendByWS(e.method))if(t.retryTimes&gt;=t.maxRetryTimesPerHour){var r=t.getHjljPostData(e);if(r&amp;&amp;r.postData){r.postData.gokey+="&amp;_j=1";var o={};i(r.postData,function(t,e){["url","logkey"].indexOf(t)===-1&amp;&amp;(o[t]=n?decodeURIComponent(e):e)}),goldlog.send(r.mmurl,o,e.method)}}else t.hjlj_callback(e)})},changeToHttpRequest:function(t){if(t&amp;&amp;t.length&gt;0)for(var e=0;e&lt;t.length;e++){var n=t[e],r=n.msg,o="object"==typeof r.postData?r.postData:JSON.parse(r.postData);o.gokey=o.gokey+"&amp;_j=1",delete o.aplus_sn,delete o.aplus_sy,delete o.ua,delete o.lang;var a=[];i(o,function(t){try{o[t]=decodeURIComponent(o[t])}catch(e){o[t]=o[t]}"pv"===n.type?"gokey"===t?(a.push("aplus"),a.push(o[t].replace(/&amp;aws=1/,""))):"pre"===t?a.push(t+"="+encodeURIComponent(o[t])):"url"!==t&amp;&amp;"logkey"!==t&amp;&amp;a.push(t+"="+o[t]):"gokey"===t&amp;&amp;(o[t]=o[t].replace(/&amp;aws=1/,""))}),"pv"===n.type?goldlog.send(r.url+"?"+a.join("&amp;")):goldlog.send(r.url,o,n.method||"GET")}},dataInArray:function(t,e){for(var n,r=0;r&lt;t.length;r++)t[r].id===e.id&amp;&amp;(n=!0);return n},reduceDataInArray:function(t,e){for(var n=[],r=0;r&lt;t.length;r++)t[r].id!==e.id&amp;&amp;n.push(t[r]);return n},msgQueueToHttpRequest:function(){var t=this.wsHandler.getMsgQueue();this.changeToHttpRequest(t),this.wsHandler.clearMsgQueue()},watchQueue:function(){var t=this;s.on(r,"beforeunload",function(){t.msgQueueToHttpRequest()}),this.wsHandler.subscribe("APLUS_WS_MSG_QUEUE_CHANGE",function(e){r.setTimeout(function(){var n=t.wsHandler.getMsgQueue();if(t.dataInArray(n,e)){t.doSetRetryTimes(),t.changeToHttpRequest([e]);var r=t.reduceDataInArray(n,e);t.wsHandler.setMsgQueue(r)}},t.timeoutToHttp)})},watchDomain:function(){var t=this;h.pushIntoGoldlogQueue("goldlog.aplus_pubsub.subscribe",["aplusInitContext",function(e){var n=e?e.where_to_sendpv:{},r=n.url.match(/(\w|-)+\.(\w|-)+\.(\w|-)+/);r&amp;&amp;r.length&gt;0&amp;&amp;(t.domain=r[0])}])},run:function(){var t={aws:1};h.pushIntoGoldlogQueue("goldlog.appendMetaInfo",["aplus-exdata",t]),h.pushIntoGoldlogQueue("goldlog.appendMetaInfo",["aplus-cpvdata",t]);try{this.retryTimes=this.getRetryTimes(),this.pageLoadDateHour=this.getDateHour(),this.startWebSocket(),this.watchLOG(),this.watchQueue(),this.watchDomain()}catch(t){g.catchException("ws_main_run_fn",t)}}})},function(t,e){"use strict";function n(){}n.prototype.extend=function(){},n.prototype.create=function(){},n.extend=function(t){return this.prototype.extend.call(this,t)},n.prototype.create=function(t){var e=new this;for(var n in t)e[n]=t[n];return e},n.prototype.extend=function(t){var e=function(){};try{"function"!=typeof Object.create&amp;&amp;(Object.create=function(t){function e(){}return e.prototype=t,new e}),e.prototype=Object.create(this.prototype);for(var n in t)e.prototype[n]=t[n];e.prototype.constructor=e,e.extend=e.prototype.extend,e.create=e.prototype.create}catch(t){console.log(t)}finally{return e}},t.exports=n},function(t,e,n){"use strict";function r(t){t=(t||"").split("#")[0].split("?")[0];var e=t.length,n=function(t){var e,n=t.length,r=0;for(e=0;e&lt;n;e++)r=31*r+t.charCodeAt(e);return r};return e?n(e+"#"+t.charCodeAt(e-1)):-1}function o(t){for(var e=t.split("&amp;"),n=0,r=e.length,o={};n&lt;r;n++){var a=e[n],s=a.indexOf("="),i=a.substring(0,s),u=a.substring(s+1);o[i]=f.tryToDecodeURIComponent(u)}return o}function a(t){if("function"!=typeof t)throw new TypeError(t+" is not a function");return t}function s(t){var e,n,r,o=[],a=t.length;for(r=0;r&lt;a;r++)e=t[r][0],n=t[r][1],o.push(l.isStartWith(e,y)?n:e+"="+encodeURIComponent(n));return o.join("&amp;")}function i(t){var e,n,r,o={},a=t.length;for(r=0;r&lt;a;r++)e=t[r][0],n=t[r][1],o[e]=n;return o}function u(t,e){var n,r,o,a=[];for(n in t)t.hasOwnProperty(n)&amp;&amp;(r=""+t[n],o=n+"="+encodeURIComponent(r),e?a.push(o):a.push(l.isStartWith(n,y)?r:o));return a.join("&amp;")}function c(t,e){var n=t.indexOf("?")==-1?"?":"&amp;",r=e?l.isArray(e)?s(e):u(e):"";return r?t+n+r:t}var l=n(4),f=n(6),h=n(9),p=parent!==self;e.is_in_iframe=p,e.makeCacheNum=l.makeCacheNum,e.isStartWith=l.isStartWith,e.isEndWith=l.isEndWith,e.any=l.any,e.each=l.each,e.assign=l.assign,e.isFunction=l.isFunction,e.isArray=l.isArray,e.isString=l.isString,e.isNumber=l.isNumber,e.isUnDefined=l.isUnDefined,e.isContain=l.isContain,e.sleep=n(10).sleep,e.makeChkSum=r,e.tryToDecodeURIComponent=f.tryToDecodeURIComponent,e.nodeListToArray=f.nodeListToArray,e.parseSemicolonContent=f.parseSemicolonContent,e.param2obj=o;var g=n(11),d=function(t){return/^(\/\/){0,1}(\w+\.){1,}\w+((\/\w+){1,})?$/.test(t)};e.hostValidity=d;var m=function(t,e){var n=/^(\/\/){0,1}(\w+\.){1,}\w+\/\w+\.gif$/.test(t),r=d(t),o="";return n?o="isGifPath":r&amp;&amp;(o="isHostPath"),o||g.logger({msg:e+": "+t+' is invalid, suggestion: "xxx.mmstat.com"'}),o},v=function(t){return!/^\/\/gj\.mmstat/.test(t)&amp;&amp;goldlog.isInternational()&amp;&amp;(t=t.replace(/^\/\/\w+\.mmstat/,"//gj.mmstat")),t};e.filterIntUrl=v,e.getPvUrl=function(t){t||(t={});var e,n,r=t.metaValue&amp;&amp;m(t.metaValue,t.metaName),o="";"isGifPath"===r?(e=/^\/\//.test(t.metaValue)?"":"//",o=e+t.metaValue):"isHostPath"===r&amp;&amp;(e=/^\/\//.test(t.metaValue)?"":"//",n=/\/$/.test(t.metaValue)?"":"/",o=e+t.metaValue+n+t.gifPath);var a;return o?a=o:(e=0===t.gifPath.indexOf("/")?t.gifPath:"/"+t.gifPath,a=t.url&amp;&amp;t.url.replace(/\/\w+\.gif/,e)),a},e.indexof=n(12).indexof,e.callable=a;var y="::-plain-::";e.mkPlainKey=function(){return y+Math.random()},e.s_plain_obj=y,e.mkPlainKeyForExparams=function(t){var e=t||y;return e+"exparams"},e.rndInt32=function(){return Math.round(2147483647*Math.random())},e.arr2param=s,e.arr2obj=i,e.obj2param=u,e.makeUrl=c,e.ifAdd=function(t,e){var n,r,o,a,s=e.length;for(n=0;n&lt;s;n++)r=e[n],o=r[0],a=r[1],a&amp;&amp;t.push([o,a])},e.isStartWithProtocol=h.isStartWithProtocol,e.param2arr=function(t){for(var e,n=t.split("&amp;"),r=0,o=n.length,a=[];r&lt;o;r++)e=n[r].split("="),a.push([e.shift(),e.join("=")]);return a},e.catchException=function(t,e,n){var r=window,o=r.goldlog_queue||(r.goldlog_queue=[]),a=t;"object"==typeof e&amp;&amp;e.message&amp;&amp;(a=a+"_"+e.message),n&amp;&amp;n.msg&amp;&amp;(a+="_"+n.msg),o.push({action:"goldlog._aplus_cplugin_m.do_tracker_jserror",arguments:[{message:a,error:JSON.stringify(e),filename:t}]})}},function(t,e,n){"use strict";function r(t,e){return"function"!=typeof Object.assign?function(t){if(null===t)throw new TypeError("Cannot convert undefined or null to object");for(var e=Object(t),n=1;n&lt;arguments.length;n++){var r=arguments[n];if(null!==r)for(var o in r)Object.prototype.hasOwnProperty.call(r,o)&amp;&amp;(e[o]=r[o])}return e}(t,e):Object.assign({},t,e)}function o(t){return"function"==typeof t}function a(t){return"string"==typeof t}function s(t){return"undefined"==typeof t}function i(t,e){return t.indexOf(e)&gt;-1}var u=window;e.assign=r,e.makeCacheNum=function(){return Math.floor(268435456*Math.random()).toString(16)},e.each=n(5),e.isStartWith=function(t,e){return 0===t.indexOf(e)},e.isEndWith=function(t,e){var n=t.length,r=e.length;return n&gt;=r&amp;&amp;t.indexOf(e)==n-r},e.any=function(t,e){var n,r=t.length;for(n=0;n&lt;r;n++)if(e(t[n]))return!0;return!1},e.isFunction=o,e.isArray=function(t){return Array.isArray?Array.isArray(t):/Array/.test(Object.prototype.toString.call(t))},e.isString=a,e.isNumber=function(t){return"number"==typeof t},e.isUnDefined=s,e.isContain=i;var c=function(t){var e,n=t.constructor===Array?[]:{};if("object"==typeof t){if(u.JSON&amp;&amp;u.JSON.parse)e=JSON.stringify(t),n=JSON.parse(e);else for(var r in t)n[r]="object"==typeof t[r]?c(t[r]):t[r];return n}};e.cloneObj=c,e.cloneDeep=c},function(t,e){"use strict";t.exports=function(t,e){var n,r=t.length;for(n=0;n&lt;r;n++)e(t[n],n)}},function(t,e,n){"use strict";var r=n(7),o=n(8);t.exports={tryToDecodeURIComponent:function(t,e){var n=e||"";if(t)try{n=decodeURIComponent(t)}catch(t){}return n},parseSemicolonContent:function(t,e,n){e=e||{};var o,a,s=t.split(";"),i=s.length;for(o=0;o&lt;i;o++){a=s[o].split("=");var u=r.trim(a.slice(1).join("="));e[r.trim(a[0])||""]=n?u:this.tryToDecodeURIComponent(u)}return e},nodeListToArray:function(t){var e,n;try{return e=[].slice.call(t)}catch(o){e=[],n=t.length;for(var r=0;r&lt;n;r++)e.push(t[r]);return e}},getLsCna:function(t,e){if(o.set&amp;&amp;o.test()){var n="",r=o.get(t);if(r){var a=r.split("_")||[];n=e?a.length&gt;1&amp;&amp;e===a[0]?a[1]:"":a.length&gt;1?a[1]:""}return decodeURIComponent(n)}return""},setLsCna:function(t,e,n){n&amp;&amp;o.set&amp;&amp;o.test()&amp;&amp;o.set(t,e+"_"+encodeURIComponent(n))},getUrl:function(t){var e=t||"//log.mmstat.com/eg.js";try{var n=goldlog.getMetaInfo("aplus-rhost-v"),r=/[[a-z|0-9\.]+[a-z|0-9]/,o=n.match(r);o&amp;&amp;o[0]&amp;&amp;(e=e.replace(r,o[0]))}catch(t){}return e}}},function(t,e){"use strict";function n(t){return"string"==typeof t?t.replace(/^\s+|\s+$/g,""):""}e.trim=n},function(t,e){"use strict";t.exports={set:function(t,e){try{return localStorage.setItem(t,e),!0}catch(t){return!1}},get:function(t){try{return localStorage.getItem(t)}catch(t){return""}},test:function(){var t="grey_test_key";try{return localStorage.setItem(t,1),localStorage.removeItem(t),!0}catch(t){return!1}},remove:function(t){localStorage.removeItem(t)}}},function(t,e,n){"use strict";var r=n(4),o=function(){if(goldlog.aplusDebug){var t=location.protocol;return"http:"!==t&amp;&amp;"https:"!==t&amp;&amp;(t="https:"),t}return"https:"};e.getProtocal=o,e.isStartWithProtocol=function(t){for(var e=["javascript:","tel:","sms:","mailto:","tmall://","#"],n=0,o=e.length;n&lt;o;n++)if(r.isStartWith(t,e[n]))return!0;return!1}},function(t,e){"use strict";e.sleep=function(t,e){return setTimeout(function(){e()},t)}},function(t,e){"use strict";var n=function(){var t=!1;return"boolean"==typeof goldlog.aplusDebug&amp;&amp;(t=goldlog.aplusDebug),t};e.isDebugAplus=n;var r=function(t){t||(t={});var e=t.level||"warn";window.console&amp;&amp;window.console[e]&amp;&amp;window.console[e](t.msg)};e.logger=r},function(t,e){"use strict";e.indexof=function(t,e){var n=-1;try{n=t.indexOf(e)}catch(o){for(var r=0;r&lt;t.length;r++)t[r]===e&amp;&amp;(n=r)}finally{return n}}},function(t,e,n){"use strict";function r(t,e,n){var r=goldlog._$||{},o=r.meta_info||{},a=o.aplus_ctap||{},s=o["aplus-touch"];if(a&amp;&amp;"function"==typeof a.on)a.on(t,e);else{var u="ontouchend"in document.createElement("div");!u||"tap"!==s&amp;&amp;"tapSpm"!==n?i(t,u?"touchstart":"mousedown",e):c.on(t,e)}}function o(t){try{f.documentElement.doScroll("left")}catch(e){return void setTimeout(function(){o(t)},1)}t()}function a(t){var e=0,n=function(){0===e&amp;&amp;t(),e++};"complete"===f.readyState&amp;&amp;n();var r;if(f.addEventListener)r=function(){f.removeEventListener("DOMContentLoaded",r,!1),n()},f.addEventListener("DOMContentLoaded",r,!1),window.addEventListener("load",n,!1);else if(f.attachEvent){r=function(){"complete"===f.readyState&amp;&amp;(f.detachEvent("onreadystatechange",r),n())},f.attachEvent("onreadystatechange",r),window.attachEvent("onload",n);var a=!1;try{a=null===window.frameElement}catch(t){}f.documentElement.doScroll&amp;&amp;a&amp;&amp;o(n)}}function s(t){"complete"===f.readyState?t():i(l,"load",t)}function i(){var t=arguments;if(2===t.length)"DOMReady"===t[0]&amp;&amp;a(t[1]),"onload"===t[0]&amp;&amp;s(t[1]);else if(3===t.length){var e=t[0],n=t[1],o=t[2];"tap"===n||"tapSpm"===n?r(e,o,n):e[d]((h?"on":"")+n,function(t){t=t||l.event;var e=t.target||t.srcElement;"function"==typeof o&amp;&amp;o(t,e)},!!u(n)&amp;&amp;{passive:!0})}}var u=n(14),c=n(15),l=window,f=document,h=!!f.attachEvent,p="attachEvent",g="addEventListener",d=h?p:g;e.DOMReady=a,e.onload=s,e.on=i},function(t,e){var n;t.exports=function(t){if("boolean"==typeof n)return n;if(!/touch|mouse|scroll|wheel/i.test(t))return!1;n=!1;try{var e=Object.defineProperty({},"passive",{get:function(){n=!0}});window.addEventListener("test",null,e)}catch(t){}return n}},function(t,e){"use strict";function n(t,e){return t+Math.floor(Math.random()*(e-t+1))}function r(t,e,n){var r=l.createEvent("HTMLEvents");if(r.initEvent(e,!0,!0),"object"==typeof n)for(var o in n)r[o]=n[o];t.dispatchEvent(r)}function o(t){0===Object.keys(h).length&amp;&amp;(f.addEventListener(d,a,!1),f.addEventListener(g,s,!1),f.addEventListener(v,s,!1));for(var e=0;e&lt;t.changedTouches.length;e++){var n=t.changedTouches[e],r={};for(var o in n)r[o]=n[o];var i={startTouch:r,startTime:Date.now(),status:m,element:t.srcElement||t.target};h[n.identifier]=i}}function a(t){for(var e=0;e&lt;t.changedTouches.length;e++){var n=t.changedTouches[e],r=h[n.identifier];if(!r)return;var o=n.clientX-r.startTouch.clientX,a=n.clientY-r.startTouch.clientY,s=Math.sqrt(Math.pow(o,2)+Math.pow(a,2));(r.status===m||"pressing"===r.status)&amp;&amp;s&gt;10&amp;&amp;(r.status="panning")}}function s(t){for(var e=0;e&lt;t.changedTouches.length;e++){var n=t.changedTouches[e],o=n.identifier,i=h[o];i&amp;&amp;(i.status===m&amp;&amp;t.type===g&amp;&amp;(i.timestamp=Date.now(),r(i.element,y,{touch:n,touchEvent:t})),delete h[o])}0===Object.keys(h).length&amp;&amp;(f.removeEventListener(d,a,!1),f.removeEventListener(g,s,!1),f.removeEventListener(v,s,!1))}function i(t){t.__fixTouchEvent||(t.addEventListener(p,function(){},!1),t.__fixTouchEvent=!0)}function u(){c||(f.addEventListener(p,o,!1),c=!0)}var c=!1,l=window.document,f=l.documentElement,h={},p="touchstart",g="touchend",d="touchmove",m="tapping",v="touchcancel",y="aplus_tap"+n(1,1e5);t.exports={on:function(t,e){u(),t&amp;&amp;t.addEventListener&amp;&amp;e&amp;&amp;(i(t),t.addEventListener(y,e._aplus_tap_callback=function(t){e(t,t.target)},!1))},un:function(t,e){t&amp;&amp;t.removeEventListener&amp;&amp;e&amp;&amp;e._aplus_tap_callback&amp;&amp;t.removeEventListener(y,e._aplus_tap_callback,!1)}}},function(t,e){"use strict";t.exports=function(t,e){if(Object&amp;&amp;Object.keys)for(var n=Object.keys(t),r=n.length,o=0;o&lt;r;o++){var a=n[o];e(a,t[a])}else for(var s in t)e(s,t[s])}},function(t,e){"use strict";function n(t,e,n){var r=""+Math.abs(t),o=e-r.length,a=t&gt;=0;return(a?n?"+":"":"-")+Math.pow(10,Math.max(0,o)).toString().substr(1)+r}e.getFormatDate=function(t){var e=new Date;try{return[e.getFullYear(),n(e.getMonth()+1,2,0),n(e.getDate(),2,0)].join(t||"")}catch(t){return""}}},function(t,e,n){"use strict";function r(t){var e=i.cookie.match(new RegExp("(?:^|;)\\s*"+t+"=([^;]+)"));return e?e[1]:""}function o(t,e,n){n||(n={});var o=new Date;return"session"===n.expires||(n.expires&amp;&amp;("number"==typeof n.expires||n.expires.toUTCString)?("number"==typeof n.expires?o.setTime(o.getTime()+24*n.expires*60*60*1e3):o=n.expires,e+="; expires="+o.toUTCString()):(o.setTime(o.getTime()+63072e7),e+="; expires="+o.toUTCString())),e+="; path="+(n.path?n.path:"/"),e+="; domain="+n.domain,n.SameSite&amp;&amp;/Chrome\/8\d+/.test(navigator.userAgent)&amp;&amp;(e+="; SameSite="+n.SameSite,e+="; Secure"),i.cookie=t+"="+e,r(t)}function a(t,e,n){try{if(n||(n={}),n.domain)o(t,e,n);else for(var r=c.getDomains(),a=0;a&lt;r.length;)n.domain=r[a],o(t,e,n)?a=r.length:a++}catch(t){}}function s(){var t={};return u.each(f,function(e){t[e]=r(e)}),t.cnaui=/\btanx\.com$/.test(l)?r("cnaui"):"",t}var i=document,u=n(4),c=n(19),l=location.hostname;e.getCookie=r,e.setCookie=a;var f=["tracknick","thw","cna"];e.getData=s,e.getHng=function(){return encodeURIComponent(r("hng")||"")}},function(t,e){"use strict";e.getDomains=function(){var t=[];try{for(var e=location.hostname,n=e.split("."),r=2;r&lt;=n.length;)t.push(n.slice(n.length-r).join(".")),r++}catch(t){}return t}},function(t,e){"use strict";e.pushIntoGoldlogQueue=function(t,e){var n=window;(n.goldlog_queue||(n.goldlog_queue=[])).push({action:t,arguments:e})}},function(t,e,n){"use strict";var r=window,o="ws.mmstat.com",a=n(22),s=n(23),i=n(20);t.exports=s.extend({status:"inactive",websocket:{},wsindexPre:"wss",wsindex:0,msg_queue:[],setWsHandler:function(t){return this.websocket[this.wsindexPre+ ++this.wsindex]=new r.WebSocket(t)},getWsHandler:function(){return this.websocket[this.wsindexPre+this.wsindex]},getMsgQueue:function(){return this.msg_queue},clearMsgQueue:function(){this.msg_queue=[]},setMsgQueue:function(t){this.msg_queue=t},proessMsgQueue:function(t){var e,n=this,r=0;if(t&amp;&amp;t.length&gt;0)for(e=t.length;r&lt;e;)n.send(t.shift()),r++;else for(e=n.msg_queue.length;r&lt;e;)n.send(n.msg_queue.shift()),r++},initWebSocket:function(t){var e=this,n="https:"===location.protocol?"wss://":"ws://",r=n+t+"/ws",o="initWebSocket";try{e.cna&amp;&amp;(r+="/"+e.cna),e.params&amp;&amp;e.params.length&gt;0&amp;&amp;(r+="?"+e.params.join("&amp;"));var s=e.setWsHandler(r),i=(new Date).getTime();s.onopen=function(){e.status="active";var t=e.getMsgQueue();t.length&gt;0&amp;&amp;e.proessMsgQueue(t);var n="connTime="+((new Date).getTime()-i);a.catchException(o+"_onopen",{message:n}),e.publish("APLUS_WS_OPEN")},s.onerror=function(t){e.status="inactive";var n=t?t.target:{},r=t?t.timeStamp:"";a.catchException(o+"_onerror",{message:"targetUrl="+n.url+"&amp;readyState="+n.readyState+"&amp;timeStamp="+r}),e.publish("APLUS_WS_ERROR")},s.onclose=function(){e.status="inactive",e.publish("APLUS_WS_CLOSE")},s.onmessage=function(t){e.publish("APLUS_WS_SERVER_MSG",t.data)}}catch(t){a.catchException(o+"_exception",t),e.publish("APLUS_WS_EXCEPTION")}},readyInitWebSocket:function(){var t=this;i.pushIntoGoldlogQueue("goldlog.aplus_pubsub.subscribe",["aplusInitContext",function(){var e=t.getWsHandler();(!e||e&amp;&amp;e.readyState&gt;1)&amp;&amp;t.initWebSocket(o)}])},start:function(){var t=this.getWsHandler();(!t||t&amp;&amp;t.readyState&gt;1)&amp;&amp;(this.status="active",this.readyInitWebSocket())},stop:function(){var t=this.getWsHandler();t&amp;&amp;t.readyState&lt;=1&amp;&amp;(this.status="inactive",t.close())},sendMsg:function(t){var e=this.getWsHandler();return!(!e||1!==e.readyState)&amp;&amp;(e.send(t),!0)},processSysEvent:function(t){"active"===t.msg?this.start():"inactive"===t.msg&amp;&amp;this.stop()},processLogEvent:function(t){if("active"===this.status){var e=this.sendMsg(t.msg.postData);e||(this.msg_queue.push(t),this.publish("APLUS_WS_MSG_QUEUE_CHANGE",t))}else this.msg_queue.push(t),this.publish("APLUS_WS_MSG_QUEUE_CHANGE",t)},send:function(t){var e=this.getWsHandler();switch((!e||e.readyState&gt;1)&amp;&amp;this.start(),t.type){case"sys":this.processSysEvent(t);break;case"pv":case"goldlog":this.processLogEvent(t)}},startWS:function(){var t=this;t.start()}})},function(t,e,n){"use strict";var r=n(20);e.catchException=function(t,e){var n=t;"object"==typeof e&amp;&amp;e.message&amp;&amp;(n=n+"_"+e.message),r.pushIntoGoldlogQueue("goldlog._aplus_cplugin_m.do_tracker_jserror",[{message:n,error:JSON.stringify(e),filename:t}])}},function(t,e,n){"use strict";function r(t){if("function"!=typeof t)throw new TypeError(t+" is not a function");return t}var o=n(2),a=function(t){for(var e=t.length,n=new Array(e-1),r=1;r&lt;e;r++)n[r-1]=t[r];return n},s=o.extend({create:function(t){var e=new this;for(var n in t)e[n]=t[n];return e.handlers=[],e.pubs={},e},setHandlers:function(t){this.handlers=t},subscribe:function(t,e){r(e);var n=this,o=n.pubs||{},a=o[t]||[];if(a)for(var s=0;s&lt;a.length;s++){var i=a[s]();e.apply(n,i)}var u=n.handlers||[];return t in u||(u[t]=[]),u[t].push(e),n.setHandlers(u),n},subscribeOnce:function(t,e){r(e);var n,o=this;return this.subscribe.call(this,t,n=function(){o.unsubscribe.call(o,t,n);var r=Array.prototype.slice.call(arguments);e.apply(o,r)}),this},unsubscribe:function(t,e){r(e);var n=this.handlers[t];if(!n)return this;if("object"==typeof n&amp;&amp;n.length&gt;0){for(var o=0;o&lt;n.length;o++){var a=e.toString(),s=n[o].toString();a===s&amp;&amp;n.splice(o,1)}this.handlers[t]=n}else delete this.handlers[t];return this},publish:function(t){var e=a(arguments),n=this.handlers||[],r=n[t]?n[t].length:0;if(r&gt;0)for(var o=0;o&lt;r;o++){var s=n[t][o];s&amp;&amp;"function"==typeof s&amp;&amp;s.apply(this,e)}return this},cachePubs:function(t){var e=this.pubs||{},n=a(arguments);e[t]||(e[t]=[]),e[t].push(function(){return n})}});t.exports=s}]);/*! 2020-03-17 20:00:45 v8.13.5 */
!function(t){function e(o){if(n[o])return n[o].exports;var a=n[o]={exports:{},id:o,loaded:!1};return t[o].call(a.exports,a,a.exports,e),a.loaded=!0,a.exports}var n={};return e.m=t,e.c=n,e.p="",e(0)}([function(t,e,n){t.exports=n(1)},function(t,e,n){"use strict";!function(){var t=window,e=n(2),o=n(4);"ontouchend"in document.createElement("div")&amp;&amp;(t.goldlog_queue||(t.goldlog_queue=[])).push({action:"goldlog.setMetaInfo",arguments:["aplus-touch","tap"]});var a=function(){n(96);var e=n(98),o=n(37);if(o.doPubMsg(["goldlogReady","running"]),document.getElementsByTagName("body").length){var r="g_tb_aplus_loaded";if(t[r])return;t[r]=1,n(111).initGoldlog(e)}else setTimeout(function(){a()},50)},r=function(n,o){try{var a=Math.floor(268435456*Math.random()).toString(16),r=t.location||{},i=["page="+encodeURIComponent(r.href),"info="+encodeURIComponent(n.message),"stack="+encodeURIComponent(n&amp;&amp;n.stack?n.stack:""),"filename=aplus_core","method="+o,"cache="+a].join("&amp;"),s=r.protocol+"//gm.mmstat.com/mm.req.load?"+i;navigator&amp;&amp;navigator.sendBeacon?e.postData(s):e.sendImg(s)}catch(t){}};try{a()}catch(t){r(t,o.script_name+"@"+o.lver)}}()},function(t,e,n){"use strict";function o(t){if(!t)return"";var e=decodeURIComponent(t).match(/cache=\w+/);return e&amp;&amp;1===e.length?e[0].split("=")[1]:void 0}var a=n(3),r=window;e.sendImg=function(t,e){var n=new Image,i="_img_"+Math.random();r[i]=n;var s=function(){if(r[i])try{delete r[i]}catch(t){r[i]=void 0}};return n.onload=function(){s()},n.onerror=function(){a.do_tracker_jserror({message:"loadError",error:"",filename:"sendImg",logid:o(t)}),s()},setTimeout(function(){window[i]&amp;&amp;(a.do_tracker_jserror({message:"loadTimeout",error:e,filename:"sendImg",logid:o(t)}),window[i].src="",s())},e||3e3),n.src=t,n=null,t},e.postData=function(t,e){for(var n in e)["cna","_p_url"].indexOf(n)===-1&amp;&amp;(e[n]=encodeURIComponent(e[n]));return navigator.sendBeacon(t,JSON.stringify(e)),t}},function(t,e){"use strict";var n=function(t,e){var n=window.goldlog_queue||(window.goldlog_queue=[]);n.push({action:"goldlog._aplus_cplugin_track_deb.monitor",arguments:[{key:"APLUS_PLUGIN_DEBUG",title:"aplus_core",msg:["_error_:methodName="+e+",params="+JSON.stringify(t)],type:"updateMsg",description:e||"aplus_core"}]})},o=function(t,e,n){var o=window.goldlog_queue||(window.goldlog_queue=[]);o.push({action:["goldlog","_aplus_cplugin_m",e].join("."),arguments:[t,n]})};e.do_tracker_jserror=function(t,e){var a="do_tracker_jserror";o(t,a,e),n(t,a)},e.do_tracker_obsolete_inter=function(t,e){var a="do_tracker_obsolete_inter";o(t,a,e),n(t,a)},e.wrap=function(t){if("function"==typeof t)try{t()}catch(t){n({msg:t.message||t},"exception")}finally{}}},function(t,e,n){"use strict";var o=n(5),a=n(6),r=n(7);e.APLUS_ENV="production",e.lver=a.lver,e.toUtVersion=a.toUtVersion,e.script_name=a.script_name,e.recordTypes=o.recordTypes,e.KEY=o.KEY,e.context=r.context,e.context_prepv=r.context_prepv,e.aplus_init=n(15).plugins_init,e.plugins_pv=n(35).plugins_pv,e.plugins_prepv=n(65).plugins_prepv,e.context_hjlj=n(66),e.plugins_hjlj=n(68).plugins_hjlj,e.beforeUnload=n(78),e.initLoad=n(83),e.spmException=n(87),e.goldlog_path=n(88),e.is_auto_pv="true",e.utilPvid=n(92),e.disablePvid="false",e.mustSpmE=!0,e.LS_CNA_KEY="APLUS_CNA"},function(t,e){"use strict";e.recordTypes={hjlj:"COMMON_HJLJ",uhjlj:"DATACLICK_HJLJ",pv:"PV",prepv:"PREPV"},e.KEY={NAME_STORAGE:{REFERRER:"wm_referrer",REFERRER_PV_ID:"refer_pv_id",LOST_PV_PAGE_DURATION:"lost_pv_page_duration",LOST_PV_PAGE_SPMAB:"lost_pv_page_spmab",LOST_PV_PAGE:"lost_pv_page",LOST_PV_PAGE_MSG:"lost_pv_page_msg"}}},function(t,e){"use strict";e.lver="8.13.5",e.toUtVersion="v20200317",e.script_name="aplus_std"},function(t,e,n){"use strict";e.context=n(8),e.context_prepv=n(14)},function(t,e,n){"use strict";function o(){return{compose:{maxTimeout:5500},etag:{egUrl:"log.mmstat.com/eg.js",cna:i.getCookie("cna")}}}function a(){return r.assign(new s.initConfig,new o)}var r=n(9),i=n(11),s=n(13);t.exports=a},function(t,e,n){"use strict";function o(t,e){return"function"!=typeof Object.assign?function(t){if(null===t)throw new TypeError("Cannot convert undefined or null to object");for(var e=Object(t),n=1;n&lt;arguments.length;n++){var o=arguments[n];if(null!==o)for(var a in o)Object.prototype.hasOwnProperty.call(o,a)&amp;&amp;(e[a]=o[a])}return e}(t,e):Object.assign({},t,e)}function a(t){return"function"==typeof t}function r(t){return"string"==typeof t}function i(t){return"undefined"==typeof t}function s(t,e){return t.indexOf(e)&gt;-1}var u=window;e.assign=o,e.makeCacheNum=function(){return Math.floor(268435456*Math.random()).toString(16)},e.each=n(10),e.isStartWith=function(t,e){return 0===t.indexOf(e)},e.isEndWith=function(t,e){var n=t.length,o=e.length;return n&gt;=o&amp;&amp;t.indexOf(e)==n-o},e.any=function(t,e){var n,o=t.length;for(n=0;n&lt;o;n++)if(e(t[n]))return!0;return!1},e.isFunction=a,e.isArray=function(t){return Array.isArray?Array.isArray(t):/Array/.test(Object.prototype.toString.call(t))},e.isString=r,e.isNumber=function(t){return"number"==typeof t},e.isUnDefined=i,e.isContain=s;var c=function(t){var e,n=t.constructor===Array?[]:{};if("object"==typeof t){if(u.JSON&amp;&amp;u.JSON.parse)e=JSON.stringify(t),n=JSON.parse(e);else for(var o in t)n[o]="object"==typeof t[o]?c(t[o]):t[o];return n}};e.cloneObj=c,e.cloneDeep=c},function(t,e){"use strict";t.exports=function(t,e){var n,o=t.length;for(n=0;n&lt;o;n++)e(t[n],n)}},function(t,e,n){"use strict";function o(t){var e=s.cookie.match(new RegExp("(?:^|;)\\s*"+t+"=([^;]+)"));return e?e[1]:""}function a(t,e,n){n||(n={});var a=new Date;return"session"===n.expires||(n.expires&amp;&amp;("number"==typeof n.expires||n.expires.toUTCString)?("number"==typeof n.expires?a.setTime(a.getTime()+24*n.expires*60*60*1e3):a=n.expires,e+="; expires="+a.toUTCString()):(a.setTime(a.getTime()+63072e7),e+="; expires="+a.toUTCString())),e+="; path="+(n.path?n.path:"/"),e+="; domain="+n.domain,n.SameSite&amp;&amp;/Chrome\/8\d+/.test(navigator.userAgent)&amp;&amp;(e+="; SameSite="+n.SameSite,e+="; Secure"),s.cookie=t+"="+e,o(t)}function r(t,e,n){try{if(n||(n={}),n.domain)a(t,e,n);else for(var o=c.getDomains(),r=0;r&lt;o.length;)n.domain=o[r],a(t,e,n)?r=o.length:r++}catch(t){}}function i(){var t={};return u.each(p,function(e){t[e]=o(e)}),t.cnaui=/\btanx\.com$/.test(l)?o("cnaui"):"",t}var s=document,u=n(9),c=n(12),l=location.hostname;e.getCookie=o,e.setCookie=r;var p=["tracknick","thw","cna"];e.getData=i,e.getHng=function(){return encodeURIComponent(o("hng")||"")}},function(t,e){"use strict";e.getDomains=function(){var t=[];try{for(var e=location.hostname,n=e.split("."),o=2;o&lt;=n.length;)t.push(n.slice(n.length-o).join(".")),o++}catch(t){}return t}},function(t,e,n){"use strict";function o(t,e,n){var o=window.goldlog||{},s=o.getMetaInfo("aplus-ifr-pv")+""=="1";return e?r(t)?"yt":"m":n&amp;&amp;!s?a.isContain(t,"wrating.com")?"k":i(t)||"y":i(t)||"v"}var a=n(9),r=function(t){for(var e=["youku.com","soku.com","tudou.com","laifeng.com"],n=0;n&lt;e.length;n++){var o=e[n];if(a.isContain(t,o))return!0}return!1},i=function(t){for(var e=[["scmp.com","sc"],["luxehomes.com.hk","sc"],["ays.com.hk","sc"],["cpjobs.com","sc"],["educationpost.com.hk","sc"],["cosmopolitan.com.hk","sc"],["elle.com.hk","sc"],["harpersbazaar.com.hk","sc"],["1688.com","6"],["youku.com","yt"],["soku.com","yt"],["tudou.com","yt"],["laifeng.com","yt"]],n=0;n&lt;e.length;n++){var o=e[n];if(a.isContain(t,o[0]))return o[1]}return""};e.getBeaconSrc=o,e.initConfig=function(){return{compose:{},etag:{egUrl:"log.mmstat.com/eg.js",cna:"",tag:"",stag:"",lstag:"-1",lscnastatus:""},can_to_sendpv:{flag:"NO"},userdata:{},what_to_sendpv:{pvdata:{},exparams:{}},what_to_pvhash:{hash:[]},what_to_sendpv_ut:{pvdataToUt:{}},what_to_sendpv_ut2:{isSuccess:!1,pvdataToUt:{}},when_to_sendpv:{aplusWaiting:""},where_to_sendpv:{url:"//log.mmstat.com/o.gif",urlRule:o},where_to_sendlog_ut:{aplusToUT:{},toUTName:"toUT"},hjlj:{what_to_hjlj:{logdata:{}},what_to_hjlj_ut:{logdataToUT:{}}},network:{connType:"UNKNOWN"},is_single:!1}}},function(t,e,n){"use strict";function o(){return{etag:{egUrl:"log.mmstat.com/eg.js",cna:a.getCookie("cna"),tag:"",stag:""},compose:{},where_to_prepv:{url:"//log.mmstat.com/v.gif",urlRule:r.getBeaconSrc},userdata:{},what_to_prepv:{logdata:{}},what_to_hjlj_exinfo:{EXPARAMS_FLAG:"EXPARAMS",exinfo:[],exparams_key_names:["uidaplus","pc_i","pu_i"]},is_single:!1}}var a=n(11),r=n(13);t.exports=o},function(t,e,n){"use strict";e.plugins_init=[{name:"where_to_sendpv",enable:!0,path:n(16)},{name:"etag",enable:!0,path:n(31)},{name:"etag_sync",enable:!0,path:n(34)}]},function(t,e,n){"use strict";var o=n(17),a=n(25),r=n(26);t.exports=function(){return{init:function(t){this.options=t},getMetaInfo:function(){var t=a.getGoldlogVal("_$")||{},e=t.meta_info||r.getInfo();return e},getAplusMetaByKey:function(t){var e=this.getMetaInfo()||{};return e[t]},getGifPath:function(t,e){var n,r=a.getGoldlogVal("_$")||{};if("function"==typeof t)n=t(location.hostname,r.is_terminal,o.is_in_iframe)+".gif";else if(!n&amp;&amp;e){var i=e.match(/\/\w+\.gif/);i&amp;&amp;i.length&gt;0&amp;&amp;(n=i[0])}return n||(n=r.is_terminal?"m.gif":"v.gif"),n},run:function(){var t=!!this.options.context.is_single;if(!t){var e=this.getAplusMetaByKey("aplus-rhost-v"),n=this.options.context.where_to_sendpv||{},a=n.url||"",r=this.getGifPath(n.urlRule,a),i=o.getPvUrl({metaName:"aplus-rhost-v",metaValue:e,gifPath:r,url:o.filterIntUrl(a)});n.url=i,this.options.context.where_to_sendpv=n}}}}},function(t,e,n){"use strict";function o(t){t=(t||"").split("#")[0].split("?")[0];var e=t.length,n=function(t){var e,n=t.length,o=0;for(e=0;e&lt;n;e++)o=31*o+t.charCodeAt(e);return o};return e?n(e+"#"+t.charCodeAt(e-1)):-1}function a(t){for(var e=t.split("&amp;"),n=0,o=e.length,a={};n&lt;o;n++){var r=e[n],i=r.indexOf("="),s=r.substring(0,i),u=r.substring(i+1);a[s]=p.tryToDecodeURIComponent(u)}return a}function r(t){if("function"!=typeof t)throw new TypeError(t+" is not a function");return t}function i(t){var e,n,o,a=[],r=t.length;for(o=0;o&lt;r;o++)e=t[o][0],n=t[o][1],a.push(l.isStartWith(e,v)?n:e+"="+encodeURIComponent(n));return a.join("&amp;")}function s(t){var e,n,o,a={},r=t.length;for(o=0;o&lt;r;o++)e=t[o][0],n=t[o][1],a[e]=n;return a}function u(t,e){var n,o,a,r=[];for(n in t)t.hasOwnProperty(n)&amp;&amp;(o=""+t[n],a=n+"="+encodeURIComponent(o),e?r.push(a):r.push(l.isStartWith(n,v)?o:a));return r.join("&amp;")}function c(t,e){var n=t.indexOf("?")==-1?"?":"&amp;",o=e?l.isArray(e)?i(e):u(e):"";return o?t+n+o:t}var l=n(9),p=n(18),g=n(21),f=parent!==self;e.is_in_iframe=f,e.makeCacheNum=l.makeCacheNum,e.isStartWith=l.isStartWith,e.isEndWith=l.isEndWith,e.any=l.any,e.each=l.each,e.assign=l.assign,e.isFunction=l.isFunction,e.isArray=l.isArray,e.isString=l.isString,e.isNumber=l.isNumber,e.isUnDefined=l.isUnDefined,e.isContain=l.isContain,e.sleep=n(22).sleep,e.makeChkSum=o,e.tryToDecodeURIComponent=p.tryToDecodeURIComponent,e.nodeListToArray=p.nodeListToArray,e.parseSemicolonContent=p.parseSemicolonContent,e.param2obj=a;var d=n(23),_=function(t){return/^(\/\/){0,1}(\w+\.){1,}\w+((\/\w+){1,})?$/.test(t)};e.hostValidity=_;var h=function(t,e){var n=/^(\/\/){0,1}(\w+\.){1,}\w+\/\w+\.gif$/.test(t),o=_(t),a="";return n?a="isGifPath":o&amp;&amp;(a="isHostPath"),a||d.logger({msg:e+": "+t+' is invalid, suggestion: "xxx.mmstat.com"'}),a},m=function(t){return!/^\/\/gj\.mmstat/.test(t)&amp;&amp;goldlog.isInternational()&amp;&amp;(t=t.replace(/^\/\/\w+\.mmstat/,"//gj.mmstat")),t};e.filterIntUrl=m,e.getPvUrl=function(t){t||(t={});var e,n,o=t.metaValue&amp;&amp;h(t.metaValue,t.metaName),a="";"isGifPath"===o?(e=/^\/\//.test(t.metaValue)?"":"//",a=e+t.metaValue):"isHostPath"===o&amp;&amp;(e=/^\/\//.test(t.metaValue)?"":"//",n=/\/$/.test(t.metaValue)?"":"/",a=e+t.metaValue+n+t.gifPath);var r;return a?r=a:(e=0===t.gifPath.indexOf("/")?t.gifPath:"/"+t.gifPath,r=t.url&amp;&amp;t.url.replace(/\/\w+\.gif/,e)),r},e.indexof=n(24).indexof,e.callable=r;var v="::-plain-::";e.mkPlainKey=function(){return v+Math.random()},e.s_plain_obj=v,e.mkPlainKeyForExparams=function(t){var e=t||v;return e+"exparams"},e.rndInt32=function(){return Math.round(2147483647*Math.random())},e.arr2param=i,e.arr2obj=s,e.obj2param=u,e.makeUrl=c,e.ifAdd=function(t,e){var n,o,a,r,i=e.length;for(n=0;n&lt;i;n++)o=e[n],a=o[0],r=o[1],r&amp;&amp;t.push([a,r])},e.isStartWithProtocol=g.isStartWithProtocol,e.param2arr=function(t){for(var e,n=t.split("&amp;"),o=0,a=n.length,r=[];o&lt;a;o++)e=n[o].split("="),r.push([e.shift(),e.join("=")]);return r},e.catchException=function(t,e,n){var o=window,a=o.goldlog_queue||(o.goldlog_queue=[]),r=t;"object"==typeof e&amp;&amp;e.message&amp;&amp;(r=r+"_"+e.message),n&amp;&amp;n.msg&amp;&amp;(r+="_"+n.msg),a.push({action:"goldlog._aplus_cplugin_m.do_tracker_jserror",arguments:[{message:r,error:JSON.stringify(e),filename:t}]})}},function(t,e,n){"use strict";var o=n(19),a=n(20);t.exports={tryToDecodeURIComponent:function(t,e){var n=e||"";if(t)try{n=decodeURIComponent(t)}catch(t){}return n},parseSemicolonContent:function(t,e,n){e=e||{};var a,r,i=t.split(";"),s=i.length;for(a=0;a&lt;s;a++){r=i[a].split("=");var u=o.trim(r.slice(1).join("="));e[o.trim(r[0])||""]=n?u:this.tryToDecodeURIComponent(u)}return e},nodeListToArray:function(t){var e,n;try{return e=[].slice.call(t)}catch(a){e=[],n=t.length;for(var o=0;o&lt;n;o++)e.push(t[o]);return e}},getLsCna:function(t,e){if(a.set&amp;&amp;a.test()){var n="",o=a.get(t);if(o){var r=o.split("_")||[];n=e?r.length&gt;1&amp;&amp;e===r[0]?r[1]:"":r.length&gt;1?r[1]:""}return decodeURIComponent(n)}return""},setLsCna:function(t,e,n){n&amp;&amp;a.set&amp;&amp;a.test()&amp;&amp;a.set(t,e+"_"+encodeURIComponent(n))},getUrl:function(t){var e=t||"//log.mmstat.com/eg.js";try{var n=goldlog.getMetaInfo("aplus-rhost-v"),o=/[[a-z|0-9\.]+[a-z|0-9]/,a=n.match(o);a&amp;&amp;a[0]&amp;&amp;(e=e.replace(o,a[0]))}catch(t){}return e}}},function(t,e){"use strict";function n(t){return"string"==typeof t?t.replace(/^\s+|\s+$/g,""):""}e.trim=n},function(t,e){"use strict";t.exports={set:function(t,e){try{return localStorage.setItem(t,e),!0}catch(t){return!1}},get:function(t){try{return localStorage.getItem(t)}catch(t){return""}},test:function(){var t="grey_test_key";try{return localStorage.setItem(t,1),localStorage.removeItem(t),!0}catch(t){return!1}},remove:function(t){localStorage.removeItem(t)}}},function(t,e,n){"use strict";var o=n(9),a=function(){if(goldlog.aplusDebug){var t=location.protocol;return"http:"!==t&amp;&amp;"https:"!==t&amp;&amp;(t="https:"),t}return"https:"};e.getProtocal=a,e.isStartWithProtocol=function(t){for(var e=["javascript:","tel:","sms:","mailto:","tmall://","#"],n=0,a=e.length;n&lt;a;n++)if(o.isStartWith(t,e[n]))return!0;return!1}},function(t,e){"use strict";e.sleep=function(t,e){return setTimeout(function(){e()},t)}},function(t,e){"use strict";var n=function(){var t=!1;return"boolean"==typeof goldlog.aplusDebug&amp;&amp;(t=goldlog.aplusDebug),t};e.isDebugAplus=n;var o=function(t){t||(t={});var e=t.level||"warn";window.console&amp;&amp;window.console[e]&amp;&amp;window.console[e](t.msg)};e.logger=o},function(t,e){"use strict";e.indexof=function(t,e){var n=-1;try{n=t.indexOf(e)}catch(a){for(var o=0;o&lt;t.length;o++)t[o]===e&amp;&amp;(n=o)}finally{return n}}},function(t,e){"use strict";var n=function(t){var e;try{window.goldlog||(window.goldlog={}),e=window.goldlog[t]}catch(t){e=""}finally{return e}};e.getGoldlogVal=n;var o=function(t,e){var n=!1;try{window.goldlog||(window.goldlog={}),t&amp;&amp;(window.goldlog[t]=e,n=!0)}catch(t){n=!1}finally{return n}};e.setGoldlogVal=o,e.getClientInfo=function(){return n("_aplus_client")||{}}},function(t,e,n){"use strict";function o(t){var e,n,o,a=t.length,r={};for(f._microscope_data=r,e=0;e&lt;a;e++)n=t[e],"microscope-data"===l.tryToGetAttribute(n,"name")&amp;&amp;(o=l.tryToGetAttribute(n,"content"),u.parseSemicolonContent(o,r),f.is_head_has_meta_microscope_data=!0);f._microscope_data_params=u.obj2param(r),f.ms_data_page_id=r.pageId,f.ms_data_shop_id=r.shopId,f.ms_data_instance_id=r.siteInstanceId,f.ms_data_siteCategoryId=r.siteCategory,f.ms_prototype_id=r.prototypeId,f.site_instance_id_or_shop_id=f.ms_data_instance_id||f.ms_data_shop_id,f._atp_beacon_data={},f._atp_beacon_data_params=""}function a(t){var e,n=function(){var e;return document.querySelector&amp;&amp;(e=document.querySelector("meta[name=data-spm]")),c.each(t,function(t){"data-spm"===l.tryToGetAttribute(t,"name")&amp;&amp;(e=t)}),e},o=n();return o&amp;&amp;(e=l.tryToGetAttribute(o,"data-spm-protocol")),e}function r(t){var e=t.isonepage||"-1",n=e.split("|"),o=n[0],a=n[1]?n[1]:"";t.isonepage_data={isonepage:o,urlpagename:a},t["aplus-pagename"]=a}function i(){var t=p.getMetaTags();o(t),c.each(t,function(t){var e=l.tryToGetAttribute(t,"name");/^aplus/.test(e)&amp;&amp;(f[e]=p.getMetaCnt(e))}),c.each(d,function(t){f[t]=p.getMetaCnt(t)}),f.spm_protocol=a(t);var e,n,i=["aplus-rate-ahot"],s=i.length;for(e=0;e&lt;s;e++)n=i[e],f[n]=parseFloat(f[n]);return r(f),_=f||{},f}function s(){return _||i()}var u=n(17),c=n(9),l=n(27),p=n(28),g=n(29),f={},d=["ahot-aplus","isonepage","spm-id","data-spm","microscope-data"],_={};e.setMetaInfo=function(t,e){return _||(_={}),_[t]=e,!0};var h=function(t){return _||(_={}),_[t]||""};e.getMetaInfo=h,e.getInfo=i,e.qGet=s,e.appendMetaInfo=function(t,e){var n=function(t,e){goldlog.setMetaInfo(t,e,{from:"appendMetaInfo"})};if(t&amp;&amp;e){var o,a=function(o){try{var a="string"==typeof e?JSON.parse(e):e;n(t,c.assign(o,a))}catch(t){}},r=function(o){try{var a="string"==typeof e?JSON.parse(e):e;n(t,o.concat(a))}catch(t){}},i=function(t){return"EXPARAMS"===t?g.getExparamsInfos("",t):t?t.split("&amp;"):[]},s=function(o){try{var a=i(o),r=i(e);n(t,a.concat(r).join("&amp;"))}catch(t){}},u=function(t){t.constructor===Array?r(t):a(t)},l=goldlog.getMetaInfo(t);if("aplus-exinfo"===t&amp;&amp;(s(l),o=!0),l)if("object"==typeof l)u(l),o=!0;else try{var p=JSON.parse(l);"object"==typeof p&amp;&amp;(u(p),o=!0)}catch(t){}o||n(t,e)}}},function(t,e){"use strict";e.tryToGetAttribute=function(t,e){return t&amp;&amp;t.getAttribute?t.getAttribute(e)||"":""};var n=function(t,e,n){if(t&amp;&amp;t.setAttribute)try{t.setAttribute(e,n)}catch(t){}};e.tryToSetAttribute=n,e.tryToRemoveAttribute=function(t,e){if(t&amp;&amp;t.removeAttribute)try{t.removeAttribute(e)}catch(o){n(t,e,"")}}},function(t,e,n){"use strict";function o(t){return i=i||document.getElementsByTagName("head")[0],s&amp;&amp;!t?s:i?s=i.getElementsByTagName("meta"):[]}function a(t,e){var n,a,r,i=o(),s=i.length;for(n=0;n&lt;s;n++)a=i[n],u.tryToGetAttribute(a,"name")===t&amp;&amp;(r=u.tryToGetAttribute(a,e||"content"));return r||""}function r(t){var e={isonepage:"-1",urlpagename:""},n=t.qGet();if(n&amp;&amp;n.hasOwnProperty("isonepage_data"))e.isonepage=n.isonepage_data.isonepage,e.urlpagename=n.isonepage_data.urlpagename;else{var o=a("isonepage")||"-1",r=o.split("|");e.isonepage=r[0],e.urlpagename=r[1]?r[1]:""}return e}var i,s,u=n(27);e.getMetaTags=o,e.getMetaCnt=a,e.getOnePageInfo=r},function(t,e,n){"use strict";var o=n(17),a=n(30),r=n(24);e.getExparamsInfos=function(t,e){var n=[],i=t||["uidaplus","pc_i","pu_i"],s=a.getExParams(o)||"";s=s.replace(/&amp;aplus&amp;/,"&amp;");for(var u=o.param2arr(s)||[],c=function(t){return r.indexof(i,t)&gt;-1},l=0;l&lt;u.length;l++){var p=u[l],g=p[0]||"",f=p[1]||"";g&amp;&amp;f&amp;&amp;("EXPARAMS"===e||c(g))&amp;&amp;n.push(g+"="+f)}return n}},function(t,e,n){"use strict";function o(){return s||(s=g.getElementById("beacon-aplus")||g.getElementById("tb-beacon-aplus")),s}function a(t){var e=o(),n=p.tryToGetAttribute(e,"cspx");t&amp;&amp;n&amp;&amp;(t.nonce=n)}function r(t,e,n){var r="script",s=g.createElement(r);s.type="text/javascript",s.async=!0;var c=o(),l=c&amp;&amp;c.hasAttribute("crossorigin");l&amp;&amp;(s.crossOrigin="anonymous");var p="https:"===location.protocol?e||t:t;0===p.indexOf("//")&amp;&amp;(p=u.getProtocal()+p),s.src=p,n&amp;&amp;(s.id=n),a(s);var f=g.getElementsByTagName(r)[0];i=i||g.getElementsByTagName("head")[0],f?f.parentNode.insertBefore(s,f):i&amp;&amp;i.appendChild(s)}var i,s,u=n(21),c=n(9),l=n(23),p=n(27),g=document;e.getCurrentNode=o,e.addScript=r,e.loadScript=function(t,e){function n(t){o.onreadystatechange=o.onload=o.onerror=null,o=null,e(t)}var o=g.createElement("script");if(i=i||g.getElementsByTagName("head")[0],o.async=!0,"onload"in o)o.onload=n;else{var r=function(){/loaded|complete/.test(o.readyState)&amp;&amp;n()};o.onreadystatechange=r,r()}o.onerror=function(t){n(t)},o.src=t,a(o),i.appendChild(o)},e.isTouch=function(){return"ontouchend"in document.createElement("div")};var f=function(){var t=goldlog&amp;&amp;goldlog._$?goldlog._$:{},e=t.meta_info||{};return e["aplus-exparams"]||""};e.getExParamsFromMeta=f,e.getExParams=function(t){var e=o(),n=p.tryToGetAttribute(e,"exparams"),a=d(n,f(),t)||"";return a&amp;&amp;a.replace(/&amp;amp;/g,"&amp;").replace(/\buserid=/,"uidaplus=")};var d=function(t,e,n){var o="aplus&amp;sidx=aplusSidex",a=t||o;try{if(e){var r=n.param2obj(e),i=["aplus","cna","spm-cnt","spm-url","spm-pre","logtype","pre","uidaplus","asid","sidx","trid","gokey"];c.each(i,function(t){r.hasOwnProperty(t)&amp;&amp;(l.logger({msg:"Can not inject keywords: "+t}),delete r[t])}),delete r[""];var s="";if(t){var u=t.match(/aplus&amp;/).index,p=u&gt;0?n.param2obj(t.substring(0,u)):{};delete p[""],s=n.obj2param(c.assign(p,r))+"&amp;"+t.substring(u,t.length)}else s=n.obj2param(r)+"&amp;"+o;return s}return a}catch(t){return a}};e.mergeExparams=d},function(t,e,n){"use strict";var o=n(3),a=n(11),r=n(30),i=n(18),s=n(32),u=n(33),c=n(25),l=n(4);t.exports=function(){return{init:function(t){this.options=t;var e=this.options.context.etag||{};this.cna=e.cna||a.getCookie("cna"),this.setTag(0),this.setStag(-1),this.setLsTag("-1"),this.setEtag(this.cna||""),this.requesting=!1,this.today=s.getFormatDate()},setLsTag:function(t){this.lstag=t,this.options.context.etag.lstag=t},setTag:function(t){this.tag=t,this.options.context.etag.tag=t},setStag:function(t){this.stag=t,this.options.context.etag.stag=t},setEtag:function(t){this.etag=t,this.options.context.etag.cna=t,a.getCookie("cna")!==t&amp;&amp;a.setCookie("cna",t,{SameSite:"none"})},setLscnaStatus:function(t){this.options.context.etag.lscnastatus=t},run:function(t,e){var n=this;if(n.cna)return void n.setTag(1);var a=null,s=u.getUrl(this.options.context.etag||{});n.requesting=!0;var p=function(){setTimeout(function(){e()},20),clearTimeout(a)};return r.loadScript(s,function(t){var e,a;if(t&amp;&amp;"error"===t.type?(n.setStag(-3),o.do_tracker_jserror({message:"loadError",error:"",filename:"etag_ls"})):(e=c.getGoldlogVal("Etag"),e&amp;&amp;n.setEtag(e),a=c.getGoldlogVal("stag"),"undefined"!=typeof a&amp;&amp;n.setStag(a)),n.requesting){if(2===a||4===a){var r=i.getLsCna(l.LS_CNA_KEY);r?(n.setLsTag(1),n.setEtag(r)):(n.setLsTag(0),i.setLsCna(l.LS_CNA_KEY,n.today,e))}p()}}),a=setTimeout(function(){n.requesting=!1,n.setStag(-2),e()},1500),2e3}}}},function(t,e){"use strict";function n(t,e,n){var o=""+Math.abs(t),a=e-o.length,r=t&gt;=0;return(r?n?"+":"":"-")+Math.pow(10,Math.max(0,a)).toString().substr(1)+o}e.getFormatDate=function(t){var e=new Date;try{return[e.getFullYear(),n(e.getMonth()+1,2,0),n(e.getDate(),2,0)].join(t||"")}catch(t){return""}}},function(t,e,n){"use strict";var o=n(18),a=n(21);e.getUrl=function(t){var e=o.getUrl(t&amp;&amp;t.egUrl?t.egUrl:"gj.mmstat.com/eg.js"),n=e.match(/[\w+\.]+[a-z|A-Z|0-9]+\/eg.js/);return 0!==e.indexOf("http")&amp;&amp;n&amp;&amp;n.length&gt;0&amp;&amp;(e=a.getProtocal()+"//"+n[0]),e}},function(t,e,n){"use strict";var o=n(18),a=n(30),r=n(33),i=n(4),s=n(32),u=n(20);t.exports=function(){return{init:function(t){this.options=t,this.today=s.getFormatDate()},run:function(){var t=this;if(u.test()){var e=o.getLsCna(i.LS_CNA_KEY,t.today);e||setTimeout(function(){var e=r.getUrl(t.options.context.etag||{});a.loadScript(e,function(e){e&amp;&amp;"error"!==e.type&amp;&amp;o.setLsCna(i.LS_CNA_KEY,t.today,goldlog.Etag)})},1e3)}}}}},function(t,e,n){"use strict";e.plugins_pv=[{name:"etag",enable:!0,path:n(36)},{name:"when_to_sendpv",enable:!0,path:n(38)},{name:"where_to_sendlog_ut",enable:!0,path:n(39)},{name:"is_single",enable:!0,path:n(41)},{name:"what_to_pvhash",enable:!0,path:n(45)},{name:"what_to_sendpv",enable:!0,path:n(46)},{name:"what_to_sendpv_userdata",enable:!0,path:n(50),deps:["what_to_sendpv"]},{name:"what_to_sendpv_etag",enable:!0,path:n(55),deps:["etag","what_to_sendpv"]},{name:"what_to_sendpv_ut2",enable:n(56),path:n(57),deps:["where_to_sendlog_ut","is_single"]},{name:"what_to_sendpv_ut",enable:!0,path:n(58),deps:["where_to_sendlog_ut","is_single"]},{name:"what_to_pv_slog",enable:!0,path:n(59),deps:["what_to_sendpv"]},{name:"can_to_sendpv",enable:!0,path:n(60)},{name:"where_to_sendpv",enable:!0,path:n(16),deps:["is_single"]},{name:"do_sendpv",enable:!0,path:n(61),deps:["is_single","what_to_sendpv","where_to_sendpv"]},{name:"do_sendpv_ut2",enable:n(56),path:n(62),deps:["what_to_sendpv_ut2","where_to_sendlog_ut"]},{name:"do_sendpv_ut",enable:n(56),path:n(63),deps:["what_to_sendpv_ut","where_to_sendlog_ut"]},{name:"after_pv",enable:!0,path:n(64)}]},function(t,e,n){"use strict";var o=n(37);t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this;o.doSubOnceMsg("aplusInitContext",function(e){e.etag&amp;&amp;(t.options.context.etag=e.etag)})}}}},function(t,e){"use strict";var n="function",o=function(){var t=window.goldlog||{},e=t.aplus_pubsub||{},o=typeof e.publish===n;return o?e:""};e.doPubMsg=function(t){var e=o();e&amp;&amp;typeof e.publish===n&amp;&amp;e.publish.apply(e,t)},e.doCachePubs=function(t){var e=o();e&amp;&amp;typeof e.cachePubs===n&amp;&amp;e.cachePubs.apply(e,t)},e.doSubMsg=function(t,e){var a=o();a&amp;&amp;typeof a.subscribe===n&amp;&amp;a.subscribe(t,e)},e.doSubOnceMsg=function(t,e){var a=o();a&amp;&amp;typeof a.subscribeOnce===n&amp;&amp;a.subscribeOnce(t,e)}},function(t,e,n){"use strict";var o=n(25),a=n(22),r=n(26);t.exports=function(){return{init:function(t){this.options=t},getMetaInfo:function(){var t=o.getGoldlogVal("_$")||{},e=t.meta_info||r.getInfo();return e},getAplusWaiting:function(){var t=this.getMetaInfo()||{};return t["aplus-waiting"]},run:function(t,e){var n=this.options.config||{},o=this.getAplusWaiting();if(o&amp;&amp;n.is_auto)switch(o=this.getAplusWaiting()+"",this.options.context.when_to_sendpv={aplusWaiting:o},o){case"MAN":return"done";case"1":return this.options.context.when_to_sendpv.isWait=!0,a.sleep(6e3,function(){e()}),6e3;default:var r=1*o;if(r+""!="NaN")return this.options.context.when_to_sendpv.isWait=!0,a.sleep(r,function(){e()}),r}}}}},function(t,e,n){"use strict";var o=n(40);t.exports=function(){return{init:function(t){this.options=t},getAplusToUT:function(t){return{toUT2:o.getAplusToUT("toUT2",t),toUT:o.getAplusToUT("toUT",t)}},run:function(){if("Umeng4Aplus"===goldlog.aplusBridgeName)this.options.context.where_to_sendlog_ut.toUTName="toUT2";else{var t=this.getAplusToUT(this.options.config.recordType);this.options.context.where_to_sendlog_ut.aplusToUT=t}}}}},function(t,e){"use strict";var n=navigator.userAgent,o=/WindVane/i.test(n);e.is_WindVane=o;var a=function(){var t=goldlog.getMetaInfo("aplus_chnl");return!(!t||!t.isAvailable||"function"!=typeof t.toUT2&amp;&amp;"function"!=typeof t.toUT)&amp;&amp;t};e.isAplusChnl=a,e.getAplusToUT=function(t,e){var n={},r=a();if("object"==typeof r)n.bridgeName=r.bridgeName||"customBridge",n.bridgeVersion=r.bridgeVersion||r.version||"",n.isAvailable=r.isAvailable,n.toUT2=r.toUT2||r.toUT;else{var i=window.WindVane||{};if(o&amp;&amp;i&amp;&amp;i.isAvailable&amp;&amp;"function"==typeof i.call){var s=t||"toUT",u=goldlog.getMetaInfo("aplus-toUT")+"";"toUT2HC"===u&amp;&amp;"PV"===e&amp;&amp;(s=u),n={bridgeName:"WindVane",bridgeVersion:i.version||"",isAvailable:!0,toUT2:function(t,e,n,o){return i.call("WVTBUserTrack",s,t,e,n,o)}}}}return n}},function(t,e,n){"use strict";var o=n(25),a=n(42),r=n(43),i=n(4);t.exports=function(){return{init:function(t){this.options=t,this._$=o.getGoldlogVal("_$")||{},this.isBoth="1"===this._$.meta_info["aplus-both-request"],this.is_WindVane=this._$.is_WindVane},isSingle_pv:function(t){return t?!this.isBoth:!(!this.is_WindVane||!r.isSingleUaVersion()||this.isBoth)},isSingle_hjlj:function(t,e){return e?!this.isBoth:!(!this.is_WindVane||!r.isSingleSendLog(t)||this.isBoth)},isSingle_uhjlj:function(t,e){return(!t||!/^\/aplus\.99\.(\d)+$/.test(t.logkey))&amp;&amp;(e?!this.isBoth:!(!(this.is_WindVane&amp;&amp;t&amp;&amp;t.logkey&amp;&amp;r.isSingleUaVersion())||this.isBoth))},run:function(){var t=this.options.context||{},e=this.options.config||{},n=t.where_to_sendlog_ut.aplusToUT||{},o=n.toUT||{},r=n.toUT2||{},s=a.isNative4Aplus(),u=!!(o.isAvailable||r.isAvailable||s),c=t.userdata||{},l=!!t.is_single;switch(e.recordType){case i.recordTypes.uhjlj:l=this.isSingle_uhjlj(c,s);break;case i.recordTypes.hjlj:l=this.isSingle_hjlj(c,s);break;case i.recordTypes.pv:l=this.isSingle_pv(s);break;default:l=this.isSingle_pv(s)}this.options.context.is_single=u&amp;&amp;l,this.options.context.ut_is_available=u}}}},function(t,e){"use strict";var n="UT4Aplus",o="Umeng4Aplus";e.isNative4Aplus=function(){var t=goldlog.getMetaInfo("aplus-toUT"),e=goldlog.aplusBridgeName;return e===n&amp;&amp;t===n||e===o},e.haveNativeFlagInUA=function(){var t=goldlog.aplusBridgeName;if(!t&amp;&amp;"boolean"!=typeof t){var e=new RegExp([n,o].join("|"),"i"),a=navigator.userAgent.match(e);t=!!a&amp;&amp;a[0],goldlog.aplusBridgeName=t}return!!t}},function(t,e,n){"use strict";var o=n(44),a=n(42),r=function(t){var e=t.logkey.toLowerCase();0===e.indexOf("/")&amp;&amp;(e=e.substr(1));var n=t.gmkey?t.gmkey.toUpperCase():"OTHER";switch(n){case"EXP":return"2201";case"CLK":return"2101";case"SLD":return"19999";case"OTHER":default:return"19999"}},i=/\sA2U\/x/.test(window.navigator.userAgent),s=function(){return i||a.haveNativeFlagInUA()||o.webviewIsAbove({version_ios_tb:[5,11,7],version_ios_tm:[5,24,1],version_android_tb:[5,11,7],version_android_tm:[5,24,1]})};e.isSingleUaVersion=s,e.isSingleSendLog=function(t){return(!t||!/^\/fsp\.1\.1$/.test(t.logkey))&amp;&amp;!!(t&amp;&amp;t.logkey&amp;&amp;s())},e.getFunctypeValue=function(t){return e.isSingleSendLog(t)?r(t):"2101"},e.getFunctypeValue2=function(t){return r(t)}},function(t,e){"use strict";var n=function(t){var e=[0,0,0];try{if(t){var n=t[1],o=n.split(".");if(o.length&gt;2)for(var a=0;a&lt;o.length;)e[a]=parseInt(o[a]),a++}}catch(t){e=[0,0,0]}finally{return e}};e.parseVersion=n;var o=function(t,e){var n=!1;try{var o=t[0]&gt;e[0],a=t[1]&gt;e[1],r=t[2]&gt;e[2],i=t[0]===e[0],s=t[1]===e[1],u=t[2]===e[2];n=!!o||(!(!i||!a)||(!!(i&amp;&amp;s&amp;&amp;r)||!!(i&amp;&amp;s&amp;&amp;u)))}catch(t){n=!1}finally{return n}};e.isAboveVersion=o,e.webviewIsAbove=function(t,e){var a=!1;try{e||(e=navigator.userAgent);var r=e.match(/AliApp\(TB\/(\d+[._]\d+[._]\d+)/i),i=n(r),s=e.match(/AliApp\(TM\/(\d+[._]\d+[._]\d+)/i),u=n(s),c=/iPhone|iPad|iPod|ios/i.test(e),l=/android/i.test(e);c?r&amp;&amp;i?a=o(i,t.version_ios_tb):s&amp;&amp;u&amp;&amp;(a=o(u,t.version_ios_tm)):l&amp;&amp;(r&amp;&amp;i?a=o(i,t.version_android_tb):s&amp;&amp;u&amp;&amp;(a=o(u,t.version_android_tm)))}catch(t){a=!1}return a}},function(t,e,n){"use strict";var o=n(25);t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this.options.context.what_to_pvhash||{},e=o.getGoldlogVal("_$")||{},n=e.meta_info||{},a=n["aplus-pvhash"]||"",r=[];"1"===a&amp;&amp;(r=["_aqx_uri",encodeURIComponent(location.href)]),t.hash=r,this.options.context.what_to_pvhash=t}}}},function(t,e,n){"use strict";var o=n(17),a=n(9),r=n(30),i=n(25),s=n(27),u=n(11),c=n(47),l=n(48),p=n(49);t.exports=function(){return a.assign(p,{init:function(t){this.options=t,this.cookie_data||(this.cookie_data=u.getData()),this.client_info||(this.client_info=i.getClientInfo()||{});var e=location.hash;e&amp;&amp;0===e.indexOf("#")&amp;&amp;(e=e.substr(1)),this.loc_hash=e},getExParams:function(){var t=window,e=document,n=[],i=parent!==t.self,u=e.getElementById("beacon-aplus")||e.getElementById("tb-beacon-aplus"),l=s.tryToGetAttribute(u,"exparams"),p=r.mergeExparams(l,r.getExParamsFromMeta(),o)||"";p=p.replace(/&amp;amp;/g,"&amp;");var g,f,d=["taobao.com","tmall.com","etao.com","hitao.com","taohua.com","juhuasuan.com","alimama.com"];if(i){for(f=d.length,g=0;g&lt;f;g++)if(o.isContain(location.hostname,d[g]))return n.push([o.mkPlainKeyForExparams(),p]),n;p=p.replace(/\buserid=\w*&amp;?/,"")}p=p.replace(/\buserid=/,"uidaplus="),p&amp;&amp;n.push([o.mkPlainKeyForExparams(),p]);var _=a.makeCacheNum();return c.updateKey(n,"cache",_),n},getExtra:function(){var t=[],e=i.getGoldlogVal("_$")||{},n=e.meta_info||{},a=this.cookie_data||{},r=this.getClientInfo(!0)||[];return o.ifAdd(t,r),o.ifAdd(t,[["thw",a.thw],["bucket_id",l.getBucketId(n)],["urlokey",this.loc_hash],["wm_instanceid",n.ms_data_instance_id]]),t}})}},function(t,e){"use strict";function n(t,e,n){r(t,"spm-cnt",function(t){var o=t.split(".");return o[0]=goldlog.spm_ab[0],o[1]=goldlog.spm_ab[1],e?o[1]=o[1].split("/")[0]+"/"+e:o[1]=o[1].split("/")[0],n&amp;&amp;(o[4]=n),o.join(".")})}function o(t,e){var n=window.g_SPM&amp;&amp;g_SPM._current_spm;
n&amp;&amp;r(t,"spm-url",function(){return[n.a,n.b,n.c,n.d].join(".")+(e?"."+e:"")},"spm-cnt")}function a(t,e){var n,o,a,r=-1;for(n=0,o=t.length;n&lt;o;n++)if(a=t[n],a[0]===e){r=n;break}r&gt;=0&amp;&amp;t.splice(r,1)}function r(t,e,n,o){var a,r,i=t.length,s=-1,u="function"==typeof n;for(a=0;a&lt;i;a++){if(r=t[a],r[0]===e)return void(u?r[1]=n(r[1]):r[1]=n);o&amp;&amp;r[0]===o&amp;&amp;(s=a)}o&amp;&amp;(u&amp;&amp;(n=n()),s&gt;-1?t.splice(s,0,[e,n]):t.push([e,n]))}t.exports={updateSPMCnt:n,updateSPMUrl:o,updateKey:r,removeKey:a}},function(t,e,n){"use strict";function o(t,e){var n,o=2146271213;for(n=0;n&lt;t.length;n++)o=(o&lt;&lt;5)+o+t.charCodeAt(n);return(65535&amp;o)%e}function a(t){var e,n=r.getCookie("t");return"3"!=t.ms_prototype_id&amp;&amp;"5"!=t.ms_prototype_id||(e=n?o(n,20):""),e}var r=n(11);e.getBucketId=a},function(t,e,n){"use strict";var o=n(17),a=n(9),r=n(25),i=n(40),s=n(11),u=n(4);t.exports={init:function(t){this.options=t,this.cookie_data||(this.cookie_data=s.getData())},getBasicParams:function(){var t=document,e=r.getGoldlogVal("_$")||{},n=e.spm||{},a=e.meta_info||{},i=a["aplus-ifr-pv"]+""=="1",u=o.is_in_iframe&amp;&amp;!i?0:1,c=this.options.config||{},l=t.title;c.title&amp;&amp;(l+="_"+c.title);var p=[["logtype",u],["title",l],["pre",e.page_referrer||""],["scr",screen.width+"x"+screen.height]],g=navigator.userAgent,f=/Safari/.test(g)&amp;&amp;!/Chrome/.test(g);f&amp;&amp;p.push(["_p_url",location.href]);var d=this.cookie_data||{},_=this.options.context||{},h=_.etag||{},m=h.cna||d.cna||s.getCookie("cna");m&amp;&amp;p.push([o.mkPlainKey(),"cna="+m]),d.tracknick&amp;&amp;p.push([o.mkPlainKey(),"nick="+d.tracknick]);var v=n.spm_url||"";return o.ifAdd(p,[["wm_pageid",a.ms_data_page_id],["wm_prototypeid",a.ms_prototype_id],["wm_sid",a.ms_data_shop_id],["spm-url",v],["spm-pre",n.spm_pre],["spm-cnt",n.spm_cnt],["cnaui",d.cnaui]]),p},getExParams:function(){return[]},getExtra:function(){return[]},getClientInfo:function(t){var e=[],n=r.getGoldlogVal("_$")||{},s=this.client_info||{},c=s.ua_info||{};if(t||!i.is_WindVane&amp;&amp;!i.isAplusChnl()){for(var l,p=[],g=["p","o","b","s","w","wx","ism"],f=0;l=g[f++];)c[l]&amp;&amp;p.push([l,c[l]]);o.ifAdd(e,p)}o.ifAdd(e,[["cache",a.makeCacheNum()],["lver",goldlog.lver||u.lver],["jsver",n.script_name||u.script_name],["pver",goldlog.aplus_cplugin_ver]]);var d=this.options.config||{},_=d.is_auto;return _||o.ifAdd(e,[["mansndlog",1]]),e},processLodashDollar:function(){var t=r.getGoldlogVal("_$")||{};t.page_url!==location.href&amp;&amp;(t.page_referrer=t.page_url,t.page_url=location.href),r.setGoldlogVal("_$",t)},getLsParams:function(){var t=r.getGoldlogVal("_$")||{},e=[];return t.lsparams&amp;&amp;t.lsparams.spm_id&amp;&amp;(e.push(["lsparams",t.lsparams.spm_id]),e.push(["lsparams_pre",t.lsparams.current_url])),e},run:function(){var t=this.getBasicParams()||[],e=this.getExParams()||[],n=this.getExtra()||[];this.processLodashDollar();var o=this.getLsParams()||[],a=[].concat(t,e,n,o);this.options.context.what_to_sendpv.pvdata=a,this.options.context.what_to_sendpv.exparams=e}}},function(t,e,n){"use strict";var o=n(17),a=n(25),r=n(47),i=n(11),s=n(51);t.exports=function(){return{init:function(t){this.options=t},getPageId:function(){var t=this.options.config||{},e=this.options.context||{},n=e.userdata||{};return t.page_id||t.pageid||t.pageId||n.page_id},getPageInfo:function(){var t;try{var e=top.location!==self.location;e&amp;&amp;void 0!==window.innerWidth&amp;&amp;(t={width:window.innerWidth,height:window.innerHeight})}catch(t){}return t},getUserdata:function(){var t=a.getGoldlogVal("_$")||{},e=t.spm||{},n=this.options.context||{},r=n.userdata||{},u=this.options.config||{},c=[];if(u&amp;&amp;!u.is_auto){u.gokey&amp;&amp;c.push([o.mkPlainKey(),u.gokey]);var l=e.data.b;if(l){var p=this.getPageId();l=p?l.split("/")[0]+"/"+p:l.split("/")[0],s.setB(l);var g=e.spm_cnt.split(".");g&amp;&amp;g.length&gt;2&amp;&amp;(g[1]=l,e.spm_cnt=g.join("."))}}var f=function(t){if("object"==typeof t)for(var e in t)"object"!=typeof t[e]&amp;&amp;"function"!=typeof t[e]&amp;&amp;c.push([e,t[e]])};f(goldlog.getMetaInfo("aplus-cpvdata")),f(r);var d=i.getCookie("workno")||i.getCookie("emplId");d&amp;&amp;c.push(["workno",d]);var _=i.getHng();_&amp;&amp;c.push(["_hng",i.getHng()]);var h=this.getPageInfo();return h&amp;&amp;(c.push(["_pw",h.width]),c.push(["_ph",h.height])),c},processLodashDollar:function(){var t=this.options.config||{},e=a.getGoldlogVal("_$")||{};t&amp;&amp;t.referrer&amp;&amp;(e.page_referrer=t.referrer),a.setGoldlogVal("_$",e)},updatePre:function(t){var e=a.getGoldlogVal("_$")||{};return e.page_referrer&amp;&amp;r.updateKey(t,"pre",e.page_referrer),t},run:function(){var t=this.options.context.what_to_sendpv.pvdata,e=this.getUserdata();this.processLodashDollar();var n=t,o=this.options.context.what_to_pvhash.hash;o&amp;&amp;o.length&gt;0&amp;&amp;n.push(o),n=n.concat(e),n=this.updatePre(n);var a=this.getPageId();a&amp;&amp;r.updateSPMCnt(n,a),this.options.context.what_to_sendpv.pvdata=n,this.options.context.userdata=e}}}},function(t,e,n){"use strict";function o(){if(!s.data.a||!s.data.b){var t=r._SPM_a,e=r._SPM_b;if(t&amp;&amp;e)return t=t.replace(/^{(\w+\/)}$/g,"$1"),e=e.replace(/^{(\w+\/)}$/g,"$1"),s.is_wh_in_page=!0,void c.setAB(t,e);var n=goldlog._$.meta_info;t=n["data-spm"]||n["spm-id"]||"0";var o=t.split(".");o.length&gt;1&amp;&amp;(t=o[0],e=o[1]),c.setA(t),e&amp;&amp;c.setB(e);var a=i.getElementsByTagName("body");a=a&amp;&amp;a.length?a[0]:null,a&amp;&amp;(e=l.tryToGetAttribute(a,"data-spm"),e?c.setB(e):1===o.length&amp;&amp;c.setAB("0","0"))}}function a(){var t=s.data.a,e=s.data.b;t&amp;&amp;e&amp;&amp;(goldlog.spm_ab=[t,e])}var r=window,i=document,s={},u={};s.data=u;var c={},l=n(27),p=n(52),g=location.href,f=n(53).getRefer(),d=n(4);c.setA=function(t){s.data.a=t,a()},c.setB=function(t){s.data.b=t,a()},c.setAB=function(t,e){s.data.a=t,s.data.b=e,a()};var _=p.getSPMFromUrl,h=function(){var t=d.utilPvid.makePVId();return d.mustSpmE?t||goldlog.pvid||"":t||""},m=function(t,e){var n=t.goldlog||window.goldlog||{},a=n.meta_info||{};s.meta_protocol=a.spm_protocol;var r,i=n.spm_ab||[],u=i[0]||"0",c=i[1]||"0";"0"===u&amp;&amp;"0"===c&amp;&amp;(o(),u=s.data.a||"0",c=s.data.b||"0"),r=[s.data.a,s.data.b].join("."),s.spm_cnt=(r||"0.0")+".0.0";var l=t.send_pv_count&gt;0?h():n.pvid;l&amp;&amp;(s.spm_cnt+="."+l),n._$.spm=s,"function"==typeof e&amp;&amp;e(l)};c.spaInit=function(t,e,n,o){var a="function"==typeof o?o:function(){},r=s.spm_url,i=window.g_SPM||{},u=t._$||{},c=u.send_pv_count;m({goldlog:t,meta_info:e,send_pv_count:c},function(t){s.spm_cnt=s.data.a+"."+s.data.b+".0.0"+(t?"."+t:"");var o=e["aplus-spm-fixed"];if("1"!==o){s.spm_pre=_(f),s.origin_spm_pre=s.spm_pre,s.spm_url=_(location.href),s.origin_spm_url=s.spm_url;var u=i._current_spm||{};u&amp;&amp;u.a&amp;&amp;"0"!==u.a&amp;&amp;u.b&amp;&amp;"0"!==u.b?(s.spm_url=[u.a,u.b,u.c,u.d,u.e].join("."),s.spm_pre=r):c&gt;0&amp;&amp;n&amp;&amp;"0"!==n[0]&amp;&amp;"0"!==n[1]&amp;&amp;(s.spm_url=n.concat(["0","0"]).join("."),s.spm_pre=r),i._current_spm={}}a()})},c.init=function(t,e,n){s.spm_url=_(g),s.spm_pre=_(f),m({goldlog:t,meta_info:e},function(){"function"==typeof n&amp;&amp;n()})},c.resetSpmCntPvid=function(){var t=goldlog.spm_ab;if(t&amp;&amp;2===t.length){var e=t.join(".")+".0.0",n=h();n&amp;&amp;(e=e+"."+n),s.spm_cnt=e,s.spm_url=e,goldlog._$.spm=s}},t.exports=c},function(t,e){"use strict";function n(t,e){if(!t||!e)return"";var n,o="";try{var a=new RegExp(t+"=([^&amp;|#|?|/]+)");if("spm"===t||"scm"===t){var r=new RegExp("\\?.*"+t+"=([\\w\\.\\-\\*/]+)"),i=e.match(a),s=e.match(r),u=i&amp;&amp;2===i.length?i[1]:"",c=s&amp;&amp;2===s.length?s[1]:"";o=u&gt;c?u:c,o=decodeURIComponent(o)}else n=e.match(a),o=n&amp;&amp;2===n.length?n[1]:""}catch(t){}finally{return o}}e.getParamFromUrl=n,e.getSPMFromUrl=function(t){return n("spm",t)}},function(t,e,n){"use strict";var o=n(54).nameStorage,a=n(5);e.getRefer=function(){var t=a.KEY||{},e=t.NAME_STORAGE||{};return document.referrer||o.getItem(e.REFERRER)||""}},function(t,e){"use strict";var n=function(){function t(){var t,e=[],r=!0;for(var l in p)p.hasOwnProperty(l)&amp;&amp;(r=!1,t=p[l]||"",e.push(c(l)+s+c(t)));n.name=r?o:a+c(o)+i+e.join(u)}function e(t,e,n){t&amp;&amp;(t.addEventListener?t.addEventListener(e,n,!1):t.attachEvent&amp;&amp;t.attachEvent("on"+e,function(e){n.call(t,e)}))}var n=window;if(n.nameStorage)return n.nameStorage;var o,a="nameStorage:",r=/^([^=]+)(?:=(.*))?$/,i="?",s="=",u="&amp;",c=encodeURIComponent,l=decodeURIComponent,p={},g={};return function(t){if(t&amp;&amp;0===t.indexOf(a)){var e=t.split(/[:?]/);e.shift(),o=l(e.shift())||"";for(var n,i,s,c=e.join(""),g=c.split(u),f=0,d=g.length;f&lt;d;f++)n=g[f].match(r),n&amp;&amp;n[1]&amp;&amp;(i=l(n[1]),s=l(n[2])||"",p[i]=s)}else o=t||""}(n.name),g.setItem=function(e,n){e&amp;&amp;"undefined"!=typeof n&amp;&amp;(p[e]=String(n),t())},g.getItem=function(t){return p.hasOwnProperty(t)?p[t]:null},g.removeItem=function(e){p.hasOwnProperty(e)&amp;&amp;(p[e]=null,delete p[e],t())},g.clear=function(){p={},t()},g.valueOf=function(){return p},g.toString=function(){var t=n.name;return 0===t.indexOf(a)?t:a+t},e(n,"beforeunload",function(){t()}),g}();e.nameStorage=n},function(t,e,n){"use strict";var o=n(47);t.exports=function(){return{init:function(t){this.options=t},updateBasicParams:function(){var t=this.options.context.what_to_sendpv.pvdata||[],e=this.options.context.etag||{};return e.cna&amp;&amp;(o.updateKey(t,"cna",e.cna),this.options.context.what_to_sendpv.pvdata=t),t},addTagParams:function(){var t=this.options.context.what_to_sendpv.pvdata||[],e=this.options.context.etag||{},n=[];(e.tag||0===e.tag)&amp;&amp;n.push(["tag",e.tag]),(e.stag||0===e.stag)&amp;&amp;n.push(["stag",e.stag]),(e.lstag||0===e.lstag)&amp;&amp;n.push(["lstag",e.lstag]),n.length&gt;0&amp;&amp;(this.options.context.what_to_sendpv.pvdata=t.concat(n))},run:function(){this.updateBasicParams(),this.addTagParams()}}}},function(t,e,n){"use strict";var o=n(44),a=n(40),r=n(42),i=/\sA2U\/x/.test(window.navigator.userAgent),s=function(t){t||(t=window.navigator.userAgent);var e=goldlog.getMetaInfo("aplus-toUT")+"",n=a.isAplusChnl(),s=o.webviewIsAbove({version_ios_tb:[6,6,0],version_ios_tm:[5,28,0],version_android_tb:[6,6,2],version_android_tm:[5,32,0]},t);return s||(s=r.haveNativeFlagInUA()||i||"2"===e||"toUT2HC"===e),n&amp;&amp;"AliBCBridge"!==n.bridgeName&amp;&amp;(s=!!n.toUT2),s};e.isToUT2=s,e.isEnable=function(t,e){var n=s(e),o=!0;switch(t){case"what_to_hjlj_ut2":case"do_sendhjlj_ut2":case"what_to_sendpv_ut2":case"do_sendpv_ut2":o=!!n;break;case"what_to_hjlj_ut":case"do_sendhjlj_ut":case"what_to_sendpv_ut":case"do_sendpv_ut":o=!n}return o}},function(t,e,n){"use strict";function o(t){var e,n,o,a,r=[],s={};for(e=t.length-1;e&gt;=0;e--)n=t[e],o=n[0],o&amp;&amp;o.indexOf(i.s_plain_obj)==-1&amp;&amp;s.hasOwnProperty(o)||(a=n[1],("aplus"==o||a)&amp;&amp;(r.unshift([o,a]),s[o]=1));return r}function a(t){var e,n,o,a,r=[],u={logtype:!0,cache:!0,scr:!0,"spm-cnt":!0};for(e=t.length-1;e&gt;=0;e--)if(n=t[e],o=n[0],a=n[1],!(s.isStartWith(o,i.s_plain_obj)&amp;&amp;!s.isStartWith(o,i.mkPlainKeyForExparams())||u[o]))if(s.isStartWith(o,i.mkPlainKeyForExparams())){var c=i.param2arr(a);if("object"==typeof c&amp;&amp;c.length&gt;0)for(var l=c.length-1;l&gt;=0;l--){var p=c[l];p&amp;&amp;p[1]&amp;&amp;r.unshift([p[0],p[1]])}}else r.unshift([o,a]);return r}function r(){var t={isonepage:"-1",urlpagename:""},e=g.qGet();if(e&amp;&amp;e.hasOwnProperty("isonepage_data"))t.isonepage=e.isonepage_data.isonepage,t.urlpagename=e.isonepage_data.urlpagename;else{var n=c.getMetaCnt("isonepage")||"-1",o=n.split("|");t.isonepage=o[0],t.urlpagename=o[1]?o[1]:""}return t}var i=n(17),s=n(9),u=n(25),c=n(28),l=n(52),p=n(42),g=n(26),f=n(4),d=n(11);t.exports=function(){return{init:function(t){this.options=t},keyIsAvailable:function(t){var e=["functype","funcId","spm-cnt","spm-url","spm-pre","_ish5","_is_g2u","_h5url","cna","isonepage","lver","jsver"];return i.indexof(e,t)===-1},valIsAvailable:function(t){return"object"!=typeof t&amp;&amp;"function"!=typeof t},upUtData:function(t,e){var n=this;if(t=t?t:{},e&amp;&amp;"object"==typeof e)for(var o in e){var a=e[o];o&amp;&amp;n.valIsAvailable(a)&amp;&amp;n.keyIsAvailable(o)&amp;&amp;(t[o]=a)}return t},getToUtData:function(t){var e=u.getGoldlogVal("_$")||{},n=e.spm||{},s=this.options.context||{},c=!!s.is_single,p=s.what_to_sendpv||{},g=a(o(p.exparams||[]));g=i.arr2obj(g);var _=i.arr2obj(p.pvdata),h=a(o(s.userdata||[]));h=i.arr2obj(h);var m=location.href,v={},b=l.getParamFromUrl("scm",m)||"";b&amp;&amp;(v.scm=b);var y=l.getParamFromUrl("pg1stepk",m)||"";y&amp;&amp;(v.pg1stepk=y);var w=l.getParamFromUrl("point",m)||"";w&amp;&amp;(v.issb=1),_&amp;&amp;_.mansndlog&amp;&amp;(v.mansndlog=_.mansndlog),v=this.upUtData(v,g),v=this.upUtData(v,h);var x=r();v.functype="page",v.funcId="2001",v.url=goldlog.getMetaInfo("aplus-pagename")||location.origin+location.pathname,v._ish5="1",v._h5url=m,v._toUT=2,v._bridgeName=t.bridgeName||"",v._bridgeVersion=t.bridgeVersion||"",v["spm-cnt"]=n.spm_cnt||"",v["spm-url"]=n.spm_url||"",v["spm-pre"]=n.spm_pre||"",v.cna=d.getCookie("cna"),v.lver=goldlog.lver||f.lver,v.jsver=f.script_name,v.pver=goldlog.aplus_cplugin_ver,v.isonepage=x.isonepage;var T=goldlog.getMetaInfo("aplus-utparam");return T&amp;&amp;(v["utparam-cnt"]=JSON.stringify(T)),v._is_g2u_=c?1:2,v},run:function(){var t=this.options.context||{},e=t.what_to_sendpv_ut2||{},n=t.where_to_sendlog_ut||{},o=n.aplusToUT||{},a=o.toUT2||{};(a&amp;&amp;a.isAvailable&amp;&amp;"function"==typeof a.toUT2||p.haveNativeFlagInUA())&amp;&amp;(e.pvdataToUt=this.getToUtData(a),this.options.context.what_to_sendpv_ut2=e)}}}},function(t,e,n){"use strict";function o(t){var e,n,o,a,i=[],s={};for(e=t.length-1;e&gt;=0;e--)n=t[e],o=n[0],o&amp;&amp;o.indexOf(r.s_plain_obj)==-1&amp;&amp;s.hasOwnProperty(o)||(a=n[1],("aplus"==o||a)&amp;&amp;(i.unshift([o,a]),s[o]=1));return i}function a(t){var e,n,o,a,s=[],u={logtype:!0,cache:!0,scr:!0,"spm-cnt":!0};for(e=t.length-1;e&gt;=0;e--)if(n=t[e],o=n[0],a=n[1],!(i.isStartWith(o,r.s_plain_obj)&amp;&amp;!i.isStartWith(o,r.mkPlainKeyForExparams())||u[o]))if(i.isStartWith(o,r.mkPlainKeyForExparams())){var c=r.param2arr(a);if("object"==typeof c&amp;&amp;c.length&gt;0)for(var l=c.length-1;l&gt;=0;l--){var p=c[l];p&amp;&amp;p[1]&amp;&amp;s.unshift([p[0],p[1]])}}else s.unshift([o,a]);return s}var r=n(17),i=n(9),s=n(25),u=n(28),c=n(42),l=n(26),p=n(4),g=n(11);t.exports=function(){return{init:function(t){this.options=t},getToUtData:function(t,e){var n,i=s.getGoldlogVal("_$")||{},c=i.spm||{},f=a(o(t)),d={};try{var _=r.arr2obj(f);_._toUT=1,_._bridgeName=e.bridgeName||"",_._bridgeVersion=e.bridgeVersion||"",n=JSON.stringify(_)}catch(t){n='{"_toUT":1}'}var h=u.getOnePageInfo(l);d.functype="2001",d.urlpagename=h.urlpagename,d.url=location.href,d.spmcnt=c.spm_cnt||"",d.spmurl=c.spm_url||"",d.spmpre=c.spm_pre||"",d.lzsid="",d.cna=g.getCookie("cna"),d.extendargs=n,d.isonepage=h.isonepage;var m=this.options.context||{},v=!!m.is_single;return d._is_g2u_=v?1:2,d.version=p.toUtVersion,d.lver=goldlog.lver||p.lver,d.jsver=p.script_name,d},run:function(){var t=this.options.context||{},e=t.what_to_sendpv||{},n=e.pvdata||[],o=t.what_to_sendpv_ut||{},a=t.where_to_sendlog_ut||{},r=a.aplusToUT||{},i=r.toUT||{};(i&amp;&amp;i.isAvailable&amp;&amp;"function"==typeof i.toUT2||c.haveNativeFlagInUA())&amp;&amp;(o.pvdataToUt=this.getToUtData(n,i),this.options.context.what_to_sendpv_ut=o)}}}},function(t,e){"use strict";t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this.options.context||{},e=t.is_single?"1":"0";if(t.what_to_sendpv_ut2.pvdataToUt._slog=e,t.what_to_sendpv_ut.pvdataToUt._slog=e,t.what_to_sendpv.pvdata.push(["_slog",e]),t.ut_is_available){var n=t.is_single?"1":"2";t.what_to_sendpv.pvdata.push(["_is_g2u",n])}}}}},function(t,e,n){"use strict";var o=n(25);t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=o.getGoldlogVal("_$")||{},e=this.options.context.can_to_sendpv||{},n=t.send_pv_count||0,a=this.options.config||{};return a.is_auto&amp;&amp;n&gt;0?"done":(e.flag="YES",this.options.context.can_to_sendpv=e,t.send_pv_count=++n,void o.setGoldlogVal("_$",t))}}}},function(t,e,n){"use strict";var o=n(25),a=n(17);t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this.options.context||{},e=!!t.is_single;if(!e){var n=t.what_to_sendpv||{},r=t.where_to_sendpv||{},i=n.pvdata||[],s=goldlog.getMetaInfo("aplus-channel");if("WS-ONLY"!==s){var u=goldlog.send(r.url,a.arr2obj(i));o.setGoldlogVal("req",u)}}}}}},function(t,e,n){"use strict";var o=n(42);t.exports=function(){return{init:function(t){this.options=t},run:function(t,e){var n=this,a=this.options.context||{},r=a.what_to_sendpv_ut2||{},i=a.where_to_sendlog_ut||{},s=r.pvdataToUt||{},u=i.aplusToUT||{},c=u.toUT2;if(o.isNative4Aplus())return u.toutflag="toUT2",void(n.options.context.what_to_sendpv_ut2.isSuccess=!0);if(c&amp;&amp;"function"==typeof c.toUT2&amp;&amp;c.isAvailable)try{u.toutflag="toUT2",c.toUT2(s,function(){n.options.context.what_to_sendpv_ut2.isSuccess=!0,e("done")},function(t){n.options.context.what_to_sendpv_ut2.errorMsg=t,e()},2e3)}catch(t){e()}finally{return"pause"}}}}},function(t,e,n){"use strict";var o=n(42);t.exports=function(){return{init:function(t){this.options=t},run:function(t,e){var n=this,a=this.options.context||{},r=a.what_to_sendpv_ut||{},i=a.where_to_sendlog_ut||{},s=r.pvdataToUt||{},u=i.aplusToUT||{},c=u.toUT;if(o.isNative4Aplus())return u.toutflag="toUT",void(n.options.context.what_to_sendpv_ut.isSuccess=!0);if(c&amp;&amp;"function"==typeof c.toUT2&amp;&amp;c.isAvailable)try{u.toutflag="toUT",c.toUT2(s,function(){n.options.context.what_to_sendpv_ut.isSuccess=!0,e()},function(t){n.options.context.what_to_sendpv_ut.errorMsg=t,e()},2e3)}catch(t){e()}finally{return"pause"}}}}},function(t,e,n){"use strict";var o=n(37),a=n(25);t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=goldlog._$||{},e=this.options.context||{};a.setGoldlogVal("pv_context",e);var n=goldlog.spm_ab||[],r=n.join("."),i=t.send_pv_count,s={cna:e.etag.cna,count:i,spmab_pre:goldlog.spmab_pre};o.doPubMsg(["sendPV","complete",r,s]),o.doCachePubs(["sendPV","complete",r,s])}}}},function(t,e){"use strict";e.plugins_prepv=[]},function(t,e,n){"use strict";function o(){var t=i.getGoldlogVal("_$")||{},e="//gm.mmstat.com/";return t.is_terminal&amp;&amp;(e="//wgo.mmstat.com/"),{where_to_hjlj:{url:e,ac_atpanel:"//ac.mmstat.com/",tblogUrl:"//log.mmstat.com/"}}}function a(){return r.assign(new s,new o)}var r=n(9),i=n(25),s=n(67);t.exports=a},function(t,e,n){"use strict";function o(){return{compose:{},basic_params:{cna:a.getCookie("cna")},where_to_hjlj:{url:"//gm.mmstat.com/",ac_atpanel:"//ac.mmstat.com/",tblogUrl:"//log.mmstat.com/"},userdata:{},what_to_hjlj:{logdata:{}},what_to_pvhash:{hash:[]},what_to_hjlj_exinfo:{EXPARAMS_FLAG:"EXPARAMS",exinfo:[],exparams_key_names:["uidaplus","pc_i","pu_i"]},what_to_hjlj_ut:{logdataToUT:{}},what_to_hjlj_ut2:{isSuccess:!1,logdataToUT:{}},where_to_sendlog_ut:{aplusToUT:{},toUTName:"toUT"},network:{connType:"UNKNOWN"},is_single:!1}}var a=n(11);t.exports=o},function(t,e,n){"use strict";e.plugins_hjlj=[{name:"etag",enable:!0,path:n(36)},{name:"where_to_sendlog_ut",enable:!0,path:n(39)},{name:"is_single",enable:!0,path:n(41)},{name:"what_to_hjlj_exinfo",enable:!0,path:n(69)},{name:"what_to_pvhash",enable:!0,path:n(45)},{name:"what_to_hjlj",enable:!0,path:n(70),deps:["what_to_hjlj_exinfo","what_to_pvhash"]},{name:"what_to_hjlj_ut2",enable:n(56),path:n(71),deps:["is_single","what_to_hjlj_exinfo"]},{name:"what_to_hjlj_ut",enable:n(56),path:n(72),deps:["is_single","what_to_hjlj_exinfo"]},{name:"what_to_hjlj_slog",enable:!0,path:n(73),deps:["what_to_hjlj"]},{name:"where_to_hjlj",enable:!0,path:n(74),deps:["is_single","what_to_hjlj"]},{name:"do_sendhjlj",enable:!0,path:n(75),deps:["is_single","what_to_hjlj","where_to_hjlj"]},{name:"do_sendhjlj_ut2",enable:n(56),path:n(76),deps:["what_to_hjlj","what_to_hjlj_ut2","where_to_sendlog_ut"]},{name:"do_sendhjlj_ut",path:n(77),deps:["what_to_hjlj","what_to_hjlj_ut","where_to_sendlog_ut"]}]},function(t,e,n){"use strict";var o=n(17),a=n(30),r=n(25),i=n(25),s=n(24),u=n(11);t.exports=function(){return{init:function(t){this.options=t},getCookieUserInfo:function(){var t=[],e=u.getCookie("workno")||u.getCookie("emplId");e&amp;&amp;t.push("workno="+e);var n=u.getHng();return n&amp;&amp;t.push("_hng="+u.getHng()),t},filterExinfo:function(t){var e="";try{t&amp;&amp;("string"==typeof t?e=t.replace(/&amp;amp;/g,"&amp;").replace(/\buserid=/,"uidaplus=").replace(/&amp;aplus&amp;/,"&amp;"):"object"==typeof t&amp;&amp;(e=o.obj2param(t,!0)))}catch(t){e=t.message?t.message:""}return e},getExparamsFlag:function(){var t=this.options.context||{},e=t.what_to_hjlj_exinfo||{};return e.EXPARAMS_FLAG||"EXPARAMS"},getCustomExParams:function(t){var e="";return t!==this.getExparamsFlag()&amp;&amp;(e=this.filterExinfo(t)||""),e?e.split("&amp;"):[]},getBeaconExparams:function(t,e){var n=[],r=a.getExParams(o)||"";r=r.replace(/&amp;aplus&amp;/,"&amp;");for(var i=o.param2arr(r)||[],u=function(e){return s.indexof(t,e)&gt;-1},c=0;c&lt;i.length;c++){var l=i[c],p=l[0]||"",g=l[1]||"";p&amp;&amp;g&amp;&amp;(e===this.getExparamsFlag()||u(p))&amp;&amp;n.push(p+"="+g)}return n},getExinfo:function(t){var e=this.options.context||{},n=e.what_to_hjlj_exinfo||{},o=n.exparams_key_names||[],a=this.getBeaconExparams(o,t);return a},getExData:function(t){var e=[];if("object"==typeof t)for(var n in t){var o=t[n];n&amp;&amp;o&amp;&amp;"object"!=typeof o&amp;&amp;"function"!=typeof o&amp;&amp;e.push(n+"="+o)}return e},doConcatArr:function(t,e){return e&amp;&amp;e.length&gt;0&amp;&amp;(t=t.concat(e)),t},run:function(){try{var t=this.options.context.what_to_hjlj_exinfo||{},e=r.getGoldlogVal("_$")||{},n=e.meta_info||{},o=n["aplus-exinfo"]||"",a=n["aplus-exdata"]||"",s=[];s=this.doConcatArr(s,t.exinfo||[]),s=this.doConcatArr(s,this.getExinfo(o)),s=this.doConcatArr(s,this.getCookieUserInfo()),s=this.doConcatArr(s,this.getCustomExParams(o)),s=this.doConcatArr(s,this.getExData(a)),t.exinfo=s.join("&amp;"),this.options.context.what_to_hjlj_exinfo=t}catch(t){i.logger({msg:t?t.message:""})}}}}},function(t,e,n){"use strict";var o=n(30),a=n(17),r=n(11),i=n(9),s=n(4);t.exports=function(){return{init:function(t){this.options=t;var e=navigator.userAgent;this.isSafari=/Safari/.test(e)&amp;&amp;!/Chrome/.test(e)},getParams:function(){var t=this.options.context||{},e=t.userdata||{},n=t.basic_params||{},u=t.what_to_hjlj_exinfo||{},c=u.exinfo||"",l=t.etag||{},p=l.cna||n.cna||r.getCookie("cna"),g=e.gmkey,f="";e.gokey&amp;&amp;c?f=[e.gokey,c].join("&amp;"):e.gokey?f=e.gokey:c&amp;&amp;(f=c);var d=t.what_to_pvhash||{},_=d.hash||[];_.length&amp;&amp;(f+="&amp;"+_.join("=")),f+="&amp;jsver="+s.script_name,f+="&amp;lver="+s.lver,f+="&amp;pver="+goldlog.aplus_cplugin_ver,f+="&amp;cache="+i.makeCacheNum();var h={gmkey:g||"",gokey:f,cna:p};this.isSafari&amp;&amp;(h._p_url=location.href),e["spm-cnt"]&amp;&amp;(h["spm-cnt"]=e["spm-cnt"]),e["spm-pre"]&amp;&amp;(h["spm-pre"]=e["spm-pre"]);try{var m=o.getExParams(a),v=a.param2obj(m).uidaplus;v&amp;&amp;(h._gr_uid_=v)}catch(t){}return h},run:function(){this.options.context.what_to_hjlj.logdata=this.getParams()}}}},function(t,e,n){"use strict";var o=n(43),a=n(25),r=n(4);t.exports=function(){return{init:function(t){this.options=t},getToUtData:function(t,e){var n=a.getGoldlogVal("_$")||{},i=n.spm||{},s=this.options.context.userdata||{},u=this.options.context.basic_params||{},c=this.options.context||{},l=c.what_to_hjlj_exinfo||{},p=l.exinfo||"",g="";s.gokey&amp;&amp;p?g=[s.gokey,p].join("&amp;"):s.gokey?g=s.gokey:p&amp;&amp;(g=p);var f={};f.functype="ctrl",f.funcId=o.getFunctypeValue2({logkey:s.logkey,gmkey:s.gmkey,spm_ab:a.getGoldlogVal("spm_ab")}),f.url=goldlog.getMetaInfo("aplus-pagename")||location.origin+location.pathname,f.logkey=s.logkey,f.gokey=encodeURIComponent(g),f.gmkey=s.gmkey,f._ish5="1",f._h5url=location.href,f._is_g2u_=t?1:2,f._toUT=2,f._bridgeName=e.bridgeName||"",f._bridgeVersion=e.bridgeVersion||"",f["spm-cnt"]=i.spm_cnt||"",f["spm-url"]=i.spm_url||"",f["spm-pre"]=i.spm_pre||"",f.cna=u.cna,f.lver=r.lver,f.jsver=r.script_name,s.hasOwnProperty("autosend")&amp;&amp;(f.autosend=s.autosend);var d=goldlog.getMetaInfo("aplus-utparam");return d&amp;&amp;(f["utparam-cnt"]=JSON.stringify(d)),f},run:function(){var t=this.options.context||{},e=t.what_to_hjlj_ut2||{},n=!!t.is_single,o=t.where_to_sendlog_ut||{},a=o.aplusToUT||{},r=a.toUT2||{};e.logdataToUT=this.getToUtData(n,r),this.options.context.what_to_hjlj_ut2=e}}}},function(t,e,n){"use strict";var o=n(43),a=n(11),r=n(25),i=n(4);t.exports=function(){return{init:function(t){this.options=t},getToUtData:function(t,e){var n=r.getGoldlogVal("_$")||{},s=n.spm||{},u=this.options.context||{},c=u.userdata||{},l=u.what_to_hjlj_exinfo||{},p=l.exinfo||"",g="";c.gokey&amp;&amp;p?g=[c.gokey,p].join("&amp;"):c.gokey?g=c.gokey:p&amp;&amp;(g=p);var f={gmkey:c.gmkey,gokey:g,lver:i.lver,jsver:i.script_name,version:i.toUtVersion,spm_cnt:s.spm_cnt||"",spm_url:s.spm_url||"",spm_pre:s.spm_pre||""};f._is_g2u_=t?1:2,f._bridgeName=e.bridgeName||"",f.bridgeVersion=e.bridgeVersion||"",f._toUT=1;try{f=JSON.stringify(f),"{}"==f&amp;&amp;(f="")}catch(t){f=""}var d=n.meta_info||{},_=d.isonepage_data||{},h={};return h.functype=o.getFunctypeValue({logkey:c.logkey,gmkey:c.gmkey,spm_ab:r.getGoldlogVal("spm_ab")}),h.spmcnt=s.spm_cnt||"",h.spmurl=s.spm_url||"",h.spmpre=s.spm_pre||"",h.logkey=c.logkey,h.logkeyargs=f,h.urlpagename=_.urlpagename,h.url=location.href,h.cna=a.getCookie("cna")||"",h.extendargs="",h.isonepage=_.isonepage,h},run:function(){var t=this.options.context||{},e=!!t.is_single,n=t.what_to_hjlj_ut||{},o=t.where_to_sendlog_ut||{},a=o.aplusToUT||{},r=a.toUT||{};n.logdataToUT=this.getToUtData(e,r),this.options.context.what_to_hjlj_ut=n}}}},function(t,e){"use strict";t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this.options.context||{},e=t.is_single?"1":"0";t.what_to_hjlj_ut2.logdataToUT._slog=e,t.what_to_hjlj_ut.logdataToUT._slog=e;var n=["_slog="+e];if(t.ut_is_available){var o=t.is_single?"1":"2";n.push("_is_g2u="+o)}t.what_to_hjlj.logdata.gokey?t.what_to_hjlj.logdata.gokey+="&amp;"+n.join("&amp;"):t.what_to_hjlj.logdata.gokey=n.join("&amp;")}}}},function(t,e,n){"use strict";var o=n(17),a=n(9),r=n(25),i=n(23),s=n(26);t.exports=function(){return{init:function(t){this.options=t},getMetaInfo:function(){var t=r.getGoldlogVal("_$")||{},e=t.meta_info||s.getInfo();return e},getAplusMetaByKey:function(t){var e=this.getMetaInfo()||{};return e[t]},cramUrl:function(t){var e=r.getGoldlogVal("_$")||{},n=e.spm||{},o=this.options.context.where_to_hjlj||{},i=o.ac_atpanel,s=o.tblogUrl,u=this.options.context.what_to_hjlj||{},c=this.options.context.userdata||{},l=!0,p=c.logkey;if(!p)return{url:t,logkey_available:!1};if("ac"==p)t=i+"1.gif";else if(a.isStartWith(p,"ac-"))t=i+p.substr(3);else if(a.isStartWith(p,"/")){t+=p.substr(1);var g=u.logdata||{};g["spm-cnt"]=n.spm_cnt,g.logtype=2;try{u.logdata=g,this.options.context.what_to_hjlj=u}catch(t){}}else a.isEndWith(p,".gif")?t=s+p:l=!1;return{url:t,logkey_available:l}},can_to_sendhjlj:function(t){var e=this.options.context||{},n=e.logger||function(){},o=this.options.context.userdata||{};return!!t.logkey_available||(n({msg:"logkey: "+o.logkey+" is not legal!"}),!1)},run:function(){var t=!!this.options.context.is_single;if(!t){var e,n,a=o.filterIntUrl(this.options.context.where_to_hjlj.url),r=this.getAplusMetaByKey("aplus-rhost-g"),s=r&amp;&amp;o.hostValidity(r);s&amp;&amp;(e=/^\/\//.test(r)?"":"//",n=/\/$/.test(r)?"":"/",a=e+r+n),r&amp;&amp;!s&amp;&amp;i.logger({msg:"aplus-rhost-g: "+r+' is invalid, suggestion: "xxx.mmstat.com"'});var u=this.cramUrl(a);return this.can_to_sendhjlj(u)?void(this.options.context.where_to_hjlj.url=u.url):"done"}}}}},function(t,e,n){"use strict";var o=n(25);t.exports=function(){return{init:function(t){this.options=t},run:function(){var t=this.options.context||{},e=this.options.config||{},n=!!t.is_single;if(!n){var a=t.logger||{},r=t.what_to_hjlj||{},i=t.where_to_hjlj||{},s=r.logdata||{},u=i.url||"";u||"function"!=typeof a||a({msg:"warning: where_to_hjlj.url is null, goldlog.record failed!"});var c=goldlog.getMetaInfo("aplus-channel");if("WS-ONLY"!==c){var l=goldlog.send(i.url,s,e.method||"GET");o.setGoldlogVal("req",l)}}}}}},function(t,e,n){"use strict";var o=n(42);t.exports=function(){return{init:function(t){this.options=t},run:function(t,e){var n=this,a=this.options.context||{},r=a.logger||function(){},i=a.what_to_hjlj_ut2||{},s=a.where_to_sendlog_ut||{},u=!!a.is_single,c=i.logdataToUT||{},l=s.aplusToUT||{},p=l.toUT2;if(o.isNative4Aplus())return l.toutflag="toUT2",void(n.options.context.what_to_hjlj_ut2.isSuccess=!0);if(p&amp;&amp;"function"==typeof p.toUT2&amp;&amp;p.isAvailable)try{l.toutflag="toUT2",p.toUT2(c,function(){n.options.context.what_to_hjlj_ut2.isSuccess=!0,e()},function(t){n.options.context.what_to_hjlj_ut2.errorMsg=t,e()},2e3)}catch(t){u&amp;&amp;r({msg:"warning: singleSendHjlj toUTName = toUT2 errorMsg:"+t.message})}finally{return"pause"}}}}},function(t,e,n){"use strict";var o=n(42);t.exports=function(){return{init:function(t){this.options=t},run:function(t,e){var n=this,a=this.options.context||{},r=a.what_to_hjlj_ut2.isSuccess,i=a.logger||function(){},s=!!a.is_single,u=a.where_to_sendlog_ut||{},c=a.what_to_hjlj_ut||{},l=c.logdataToUT||{},p=u.aplusToUT||{},g=p.toUT;if(o.isNative4Aplus())return p.toutflag="toUT",void(n.options.context.what_to_hjlj_ut.isSuccess=!0);if(!r&amp;&amp;g&amp;&amp;"function"==typeof g.toUT2&amp;&amp;g.isAvailable)try{p.toutflag="toUT",g.toUT2(l,function(){n.options.context.what_to_hjlj_ut.isSuccess=!0,e()},function(t){n.options.context.what_to_hjlj_ut.errorMsg=t,e()},3e3)}catch(t){s&amp;&amp;i({msg:"warning: singleSend toUTName = "+u.toUTName+" errorMsg:"+t.message})}finally{return"pause"}}}}},function(t,e,n){"use strict";function o(){var t,e,n=i.KEY||{},o=n.NAME_STORAGE||{};if(!l&amp;&amp;c){var a=location.href,u=c&amp;&amp;(a.indexOf("login.taobao.com")&gt;=0||a.indexOf("login.tmall.com")&gt;=0),p=s.getRefer();u&amp;&amp;p?(t=p,e=r.getItem(o.REFERRER_PV_ID)):(t=a,e=goldlog.pvid),r.setItem(o.REFERRER,t),r.setItem(o.REFERRER_PV_ID,e)}}var a=n(79),r=n(54).nameStorage,i=n(4),s=n(53),u=n(82),c="https:"==location.protocol,l=parent!==self;e.run=function(){var t="beforeunload";a.on(window,t,function(){o(),u(t)})}},function(t,e,n){"use strict";function o(t,e,n){var o=goldlog._$||{},a=o.meta_info||{},r=a.aplus_ctap||{},i=a["aplus-touch"];if(r&amp;&amp;"function"==typeof r.on)r.on(t,e);else{var u="ontouchend"in document.createElement("div");!u||"tap"!==i&amp;&amp;"tapSpm"!==n?s(t,u?"touchstart":"mousedown",e):c.on(t,e)}}function a(t){try{p.documentElement.doScroll("left")}catch(e){return void setTimeout(function(){a(t)},1)}t()}function r(t){var e=0,n=function(){0===e&amp;&amp;t(),e++};"complete"===p.readyState&amp;&amp;n();var o;if(p.addEventListener)o=function(){p.removeEventListener("DOMContentLoaded",o,!1),n()},p.addEventListener("DOMContentLoaded",o,!1),window.addEventListener("load",n,!1);else if(p.attachEvent){o=function(){"complete"===p.readyState&amp;&amp;(p.detachEvent("onreadystatechange",o),n())},p.attachEvent("onreadystatechange",o),window.attachEvent("onload",n);var r=!1;try{r=null===window.frameElement}catch(t){}p.documentElement.doScroll&amp;&amp;r&amp;&amp;a(n)}}function i(t){"complete"===p.readyState?t():s(l,"load",t)}function s(){var t=arguments;if(2===t.length)"DOMReady"===t[0]&amp;&amp;r(t[1]),"onload"===t[0]&amp;&amp;i(t[1]);else if(3===t.length){var e=t[0],n=t[1],a=t[2];"tap"===n||"tapSpm"===n?o(e,a,n):e[_]((g?"on":"")+n,function(t){t=t||l.event;var e=t.target||t.srcElement;"function"==typeof a&amp;&amp;a(t,e)},!!u(n)&amp;&amp;{passive:!0})}}var u=n(80),c=n(81),l=window,p=document,g=!!p.attachEvent,f="attachEvent",d="addEventListener",_=g?f:d;e.DOMReady=r,e.onload=i,e.on=s},function(t,e){var n;t.exports=function(t){if("boolean"==typeof n)return n;if(!/touch|mouse|scroll|wheel/i.test(t))return!1;n=!1;try{var e=Object.defineProperty({},"passive",{get:function(){n=!0}});window.addEventListener("test",null,e)}catch(t){}return n}},function(t,e){"use strict";function n(t,e){return t+Math.floor(Math.random()*(e-t+1))}function o(t,e,n){var o=l.createEvent("HTMLEvents");if(o.initEvent(e,!0,!0),"object"==typeof n)for(var a in n)o[a]=n[a];t.dispatchEvent(o)}function a(t){0===Object.keys(g).length&amp;&amp;(p.addEventListener(_,r,!1),p.addEventListener(d,i,!1),p.addEventListener(m,i,!1));for(var e=0;e&lt;t.changedTouches.length;e++){var n=t.changedTouches[e],o={};for(var a in n)o[a]=n[a];var s={startTouch:o,startTime:Date.now(),status:h,element:t.srcElement||t.target};g[n.identifier]=s}}function r(t){for(var e=0;e&lt;t.changedTouches.length;e++){var n=t.changedTouches[e],o=g[n.identifier];if(!o)return;var a=n.clientX-o.startTouch.clientX,r=n.clientY-o.startTouch.clientY,i=Math.sqrt(Math.pow(a,2)+Math.pow(r,2));(o.status===h||"pressing"===o.status)&amp;&amp;i&gt;10&amp;&amp;(o.status="panning")}}function i(t){for(var e=0;e&lt;t.changedTouches.length;e++){var n=t.changedTouches[e],a=n.identifier,s=g[a];s&amp;&amp;(s.status===h&amp;&amp;t.type===d&amp;&amp;(s.timestamp=Date.now(),o(s.element,v,{touch:n,touchEvent:t})),delete g[a])}0===Object.keys(g).length&amp;&amp;(p.removeEventListener(_,r,!1),p.removeEventListener(d,i,!1),p.removeEventListener(m,i,!1))}function s(t){t.__fixTouchEvent||(t.addEventListener(f,function(){},!1),t.__fixTouchEvent=!0);
}function u(){c||(p.addEventListener(f,a,!1),c=!0)}var c=!1,l=window.document,p=l.documentElement,g={},f="touchstart",d="touchend",_="touchmove",h="tapping",m="touchcancel",v="aplus_tap"+n(1,1e5);t.exports={on:function(t,e){u(),t&amp;&amp;t.addEventListener&amp;&amp;e&amp;&amp;(s(t),t.addEventListener(v,e._aplus_tap_callback=function(t){e(t,t.target)},!1))},un:function(t,e){t&amp;&amp;t.removeEventListener&amp;&amp;e&amp;&amp;e._aplus_tap_callback&amp;&amp;t.removeEventListener(v,e._aplus_tap_callback,!1)}}},function(t,e){"use strict";t.exports=function(t){var e=goldlog&amp;&amp;goldlog._$?goldlog._$.pageLoadTime:"";if("setPageSPM"===t){goldlog.preSetPageSPMTime=goldlog.setPageSPMTime||e||"",goldlog.setPageSPMTime=(new Date).getTime();var n=goldlog.spm_ab;n&amp;&amp;"0.0"!==n&amp;&amp;goldlog.record("/x.p.d","OTHER","_s="+goldlog.preSetPageSPMTime+"&amp;_e="+goldlog.setPageSPMTime+"&amp;from="+t,"POST")}else if("beforeunload"===t){var o="";try{o=performance.timing.domInteractive}catch(t){o=e}var a=(new Date).getTime();goldlog.record("/x.p.d","OTHER","_s="+o+"&amp;_e="+a+"&amp;from="+t,"POST")}}},function(t,e,n){"use strict";function o(){var t=(new Date).getTime(),e=Math.floor(t/72e5),n=a.getElementById("aplus-sufei"),o=goldlog._$||{},s=goldlog.getCdnPath(),u=s+"/alilog/aplus_plugin_xwj/index.js?t="+e,c=s+"/alilog/oneplus/entry.js?t="+e,l=s+"/alilog/stat/a.js?t="+e,p=s+"/secdev/entry/index.js?t="+e,g=s+"/alilog/mlog/wp_beacon.js?t="+e,f=o.meta_info,d=function(){r.addScript(l),r.addScript(g),r.addScript(u),r.addScript(c)},_=function(){Math.random()&lt;.01&amp;&amp;r.addScript(l),f.ms_data_instance_id&amp;&amp;f.ms_prototype_id&amp;&amp;f.ms_prototype_id.match(/^[124]$/)&amp;&amp;f.ms_data_shop_id&amp;&amp;r.addScript(g);var t=f["aplus-rate-ahot"];(Math.random()&lt;t||f["ahot-aplus"])&amp;&amp;r.addScript(u),r.addScript(c)},h=f["aplus-xplug"];i.onload(function(){try{switch(h){case"NONE":break;case"ALL":d();break;default:_()}}catch(t){}}),"NONE"!==h&amp;&amp;setTimeout(function(){n&amp;&amp;"script"==n.tagName.toLowerCase()||r.addScript(p,"","aplus-sufei")},10)}var a=document,r=n(30),i=n(79),s=n(84);e.run=function(){o()},e.init_watchGoldlogQueue=s.init_watchGoldlogQueue},function(t,e,n){"use strict";function o(t,e){for(var n={subscribeMwChangeQueue:[],subscribeMetaQueue:[],subscribeQueue:[],metaQueue:[],othersQueue:[]},o=[],a={};a=t.shift();)try{var r=a.action,i=a.arguments[0];/subscribe/.test(r)?"setMetaInfo"===i?n.subscribeMetaQueue.push(a):"mw_change_pv"===i||"mw_change_hjlj"===i?n.subscribeMwChangeQueue.push(a):n.subscribeQueue.push(a):/MetaInfo/.test(r)?n.metaQueue.push(a):n.othersQueue.push(a)}catch(t){n.othersQueue.push(a),u.do_tracker_jserror({message:t&amp;&amp;t.message,error:encodeURIComponent(t.stack),filename:"getFormatQueue"})}var s;return e&amp;&amp;n[e]&amp;&amp;(s=n[e],n[e]=[]),o=n.subscribeMwChangeQueue.concat(n.metaQueue),o=o.concat(n.subscribeQueue),o=o.concat(n.subscribeMetaQueue,n.othersQueue),{queue:o,formatQueue:s}}var a=window,r=n(9),i=n(85),s=n(86),u=n(3),c="goldlog_queue",l=function(t,e,n){try{/_aplus_cplugin_track_deb/.test(t)||/_aplus_cplugin_m/.test(t)||u.do_tracker_jserror({message:n||'illegal task: goldlog_queue.push("'+JSON.stringify(e)+'")',error:JSON.stringify(e),filename:"processTask"})}catch(t){}},p=function(t,e){var n=t?t.action:"",o=t?t.arguments:"";try{if(n&amp;&amp;o&amp;&amp;r.isArray(o)){var i=n.split("."),s=a,u=a;if(3===i.length)s=a[i[0]][i[1]]||{},u=s[i[2]]?s[i[2]]:"";else for(;i.length;)if(u=s=s[i.shift()],!s)return void("function"==typeof e?e(t):l(n,t));"function"==typeof u&amp;&amp;u.apply(s,o)}else l(n,t)}catch(e){l(n,t,e.message)}},g=function(t){function e(){if(t&amp;&amp;r.isArray(t)&amp;&amp;t.length){for(var e=o(t).queue,n={},a=[];n=e.shift();)p(n,function(t){a.push(t)});a.length&gt;0&amp;&amp;setTimeout(function(){for(;n=a.shift();)p(n)},100)}}try{e()}catch(t){u.do_tracker_jserror({message:t&amp;&amp;t.message,error:encodeURIComponent(t.stack),filename:"processGoldlogQueue"})}};e.processGoldlogQueue=g;var f=i.extend({push:function(t){this.length++,p(t)}});e.init_watchGoldlogQueue=function(t){try{var e=a[c]||[];if(t){var n=o(e,t);a[c]=n.queue,g(n.formatQueue)}else a[c]=f.create({startLength:e.length,length:0}),s.init_loadAplusPlugin(),g(e)}catch(t){u.do_tracker_jserror({message:t&amp;&amp;t.message,error:encodeURIComponent(t.stack),filename:"init_watchGoldlogQueue"})}}},function(t,e){"use strict";function n(){}n.prototype.extend=function(){},n.prototype.create=function(){},n.extend=function(t){return this.prototype.extend.call(this,t)},n.prototype.create=function(t){var e=new this;for(var n in t)e[n]=t[n];return e},n.prototype.extend=function(t){var e=function(){};try{"function"!=typeof Object.create&amp;&amp;(Object.create=function(t){function e(){}return e.prototype=t,new e}),e.prototype=Object.create(this.prototype);for(var n in t)e.prototype[n]=t[n];e.prototype.constructor=e,e.extend=e.prototype.extend,e.create=e.prototype.create}catch(t){console.log(t)}finally{return e}},t.exports=n},function(t,e,n){"use strict";var o=n(30),a=n(28),r=n(6),i=function(){var t=goldlog.getCdnPath()+"/alilog/s/"+r.lver+"/plugin/";return{aplus_ae_path:t+"aplus_ae.js",aplus_ac_path:t+"aplus_ac.js"}},s={},u="aplus-auto-exp",c="aplus-auto-clk",l=function(t,e){var n=i(),r=goldlog&amp;&amp;goldlog.getMetaInfo?goldlog.getMetaInfo(t):"",l=e||r||a.getMetaCnt(t),p={};p[u]=n.aplus_ae_path,p[c]=n.aplus_ac_path,l&amp;&amp;p[t]&amp;&amp;!s[t]&amp;&amp;(o.addScript(p[t]),s[t]=!0)};e.init_loadAplusPlugin=function(){try{!goldlog._aplus_auto_exp&amp;&amp;l(u),!goldlog._aplus_ac&amp;&amp;l(c),goldlog.aplus_pubsub.subscribe("setMetaInfo",function(t,e){t!==u||goldlog._aplus_auto_exp||l(t,e),t!==c||goldlog._aplus_ac||l(t,e)})}catch(t){}}},function(t,e){"use strict";function n(t,e){return t.indexOf(e)&gt;-1}function o(t,e){for(var o=0,a=t.length;o&lt;a;o++)if(n(e,t[o]))return!0;return!1}var a=location.host,r=["admin.taobao.org","mybank.cn"],i=["tmc.admin.taobao.org","tmall.admin.taobao.org"];e.is_exception=o(r,a)&amp;&amp;!o(i,a)},function(t,e,n){"use strict";function o(){var t,e,n,o,a=c.getElementsByTagName("meta");for(t=0,e=a.length;t&lt;e;t++)if(n=a[t],o=n.getAttribute("name"),"data-spm"===o||"spm-id"===o)return n}function a(){var t=c.createElement("meta");t.setAttribute("name","data-spm");var e=c.getElementsByTagName("head")[0];return e&amp;&amp;e.insertBefore(t,e.firstChild),t}function r(){var t=o();t||(t=a()),t.setAttribute("content",goldlog.spm_ab[0]||"");var e=c.getElementsByTagName("body")[0];e&amp;&amp;e.setAttribute("data-spm",goldlog.spm_ab[1]||"")}function i(){var t,e,n,o=c.getElementsByTagName("*");for(t=0,e=o.length;t&lt;e;t++)n=o[t],n.getAttribute("data-spm-max-idx")&amp;&amp;n.setAttribute("data-spm-max-idx",""),n.getAttribute("data-spm-anchor-id")&amp;&amp;n.setAttribute("data-spm-anchor-id","")}function s(){var t=5e3;try{var e=goldlog.getMetaInfo("aplus-mmstat-timeout");if(e){var n=parseInt(e);n&gt;=1e3&amp;&amp;n&lt;=1e4&amp;&amp;(t=n)}}catch(t){}return t}var u=window,c=document,l=n(85),p=n(17),g=n(79),f=n(30),d=n(23),_=n(37),h=n(9),m=n(25),v=n(21),b=n(40),y=n(82),w=n(51),x=n(26),T=x.getInfo(),j=n(4),P=n(3),S=n(89),A=n(11),k=n(92),U=n(2),E=(d.isDebugAplus(),[]),M=[],I=[],C=[],N="//g.alicdn.com",V="//g-assets.daily.taobao.net",O="//assets.alicdn.com/g",G="//s.alicdn.com/@g/",L="//u.alicdn.com",R="//laz-g-cdn.alicdn.com";e.run=l.extend({getCdnPath:function(){var t=f.getCurrentNode(),e=N,n=[O,G,V,L,R],o=new RegExp(L);if(t)for(var a=0;a&lt;n.length;a++){var r=new RegExp(n[a]);if(r.test(t.src)){e=n[a],o.test(t.src)&amp;&amp;(e=O);break}}return e},isInternational:function(){this.cdnPath||(this.cdnPath=this.getCdnPath());var t=[O,G,R].indexOf(this.cdnPath)&gt;-1;return t||"int"===this.getMetaInfo("aplus-env")},getCookie:function(t){return A.getCookie(t)},getParam:function(t){var e=u.WindVane||{},n=b.isAplusChnl(),o="";n&amp;&amp;"object"==typeof n&amp;&amp;(o=n.bridgeName||"customBridge");var a=e.getParam?"WindVane":o,r=e&amp;&amp;"function"==typeof e.getParam?e.getParam(t):"",i=(goldlog.spm_ab?goldlog.spm_ab.join("."):"0.0","sid="+t+"@valueIsEmpty="+!r);return a&amp;&amp;(i+="_bridgeName="+a),r},beforeSendPV:function(t){E.push(t)},afterSendPV:function(t){M.push(t)},send:function(t,e,n){var o;if(0===t.indexOf("//")){var a=v.getProtocal();t=a+t}return o="POST"===n&amp;&amp;navigator&amp;&amp;navigator.sendBeacon?U.postData(t,e):U.sendImg(p.makeUrl(t,e),s())},launch:function(t,e){var n;try{e=h.assign(e,t),n=goldlog._$._sendPV(e,t);var o=goldlog.spm_ab?goldlog.spm_ab.join("."):"0.0";P.do_tracker_obsolete_inter({page:location.hostname+location.pathname,spm_ab:o,interface_name:"goldlog.launch",interface_params:"userdata = "+JSON.stringify(t)+", config = "+JSON.stringify(e)})}catch(t){}finally{return d.logger({msg:"warning: This interface is deprecated, please use goldlog.sendPV instead! API: http://log.alibaba-inc.com/log/info.htm?type=2277&amp;id=31"}),n}},_$:{_sendPV:function(t,e){if(t=t||{},h.any(E,function(e){return e(goldlog,t)===!1}))return!1;var o=n(94).SendPV,a=new o;return"undefined"==typeof t.recordType&amp;&amp;(t.recordType=j.recordTypes.pv),a.run(t,e,{fn_after_pv:M}),!0},_sendPseudo:function(t,e){t||(t={});var o=n(95).SendPrePV,a=new o;return"undefined"==typeof t.recordType&amp;&amp;(t.recordType=j.recordTypes.prepv),a.run(t,e,{},function(){_.doPubMsg(["sendPrePV","complete"])}),!0}},sendPV:function(t,e){return e=e||{},e.pageName&amp;&amp;goldlog.setMetaInfo("aplus-pagename",e.pageName),goldlog._$._sendPV(t,e)},updatePageProperties:function(t){t&amp;&amp;"object"==typeof t?(t._page&amp;&amp;(t.pageName=t._page,delete t._page),t.pageName&amp;&amp;(goldlog.setMetaInfo("aplus-pagename",t.pageName),delete t.pageName),goldlog.appendMetaInfo("aplus-cpvdata",t)):d.logger({msg:"warning: typeof updatePageProperties's params must be object"})},beforeRecord:function(t){I.push(t)},afterRecord:function(t){C.push(t)},record:function(t,e,n,o,a){if(!h.any(I,function(t){return t(goldlog)===!1}))return"POST"!==o&amp;&amp;"WS"!==o&amp;&amp;"WS-ONLY"!==o&amp;&amp;(o="GET"),S.run({recordType:j.recordTypes.hjlj,method:o},{logkey:t,gmkey:e,gokey:n},{fn_after_record:C},function(){"function"==typeof a&amp;&amp;a()}),!0},recordUdata:function(t,e,n,o,a){var r=m.getGoldlogVal("_$")||{},i=r.spm||{};"POST"!==o&amp;&amp;"WS"!==o&amp;&amp;"WS-ONLY"!==o&amp;&amp;(o="GET"),S.run({ignore_chksum:!0,method:o,recordType:j.recordTypes.uhjlj},{logkey:t,gmkey:e,gokey:n,"spm-cnt":i.spm_cnt,"spm-pre":i.spm_pre},{},function(){h.isFunction(a)&amp;&amp;a()})},setPageSPM:function(t,e,n){var o="setPageSPM";y(o);var a=goldlog.getMetaInfo("aplus-spm-fixed"),s="function"==typeof n?n:function(){};goldlog.spm_ab=goldlog.spm_ab||[];var u=h.cloneObj(goldlog.spm_ab);if(t&amp;&amp;(goldlog.spm_ab[0]=""+t,goldlog._$.spm.data.a=""+t),e&amp;&amp;(goldlog.spm_ab[1]=""+e,goldlog._$.spm.data.b=""+e),w.spaInit(goldlog,T,u),"1"!==a){var c=u.join(".");goldlog.spmab_pre=c}var l=goldlog.spm_ab.join(".");_.doPubMsg([o,{spmab_pre:goldlog.spmab_pre,spmab:l}]),_.doCachePubs([o,{spmab_pre:goldlog.spmab_pre,spmab:l}]),r(),i(),s()},setMetaInfo:function(t,e,n){if(x.setMetaInfo(t,e)){var o=m.getGoldlogVal("_$")||{};o.meta_info=x.qGet();var a=m.setGoldlogVal("_$",o),r=k.isDisablePvid()+"";return"aplus-disable-pvid"===t&amp;&amp;r!==e+""&amp;&amp;w.resetSpmCntPvid(),_.doPubMsg(["setMetaInfo",t,e,n]),_.doCachePubs(["setMetaInfo",t,e,n]),a}},appendMetaInfo:x.appendMetaInfo,getMetaInfo:function(t){return x.getMetaInfo(t)},on:g.on,cloneDeep:h.cloneDeep,getPvId:k.getPvId})},function(t,e,n){"use strict";var o=n(9),a=n(25),r=n(37),i=n(23),s=n(90),u=n(91),c=n(4);e.run=function(t,e,n,l){var p=new u;p.init({middleware:[],config:t,plugins:c.plugins_hjlj});var g=p.run(),f=new c.context_hjlj;f.userdata=e,f.logger=i.logger;var d={context:f,pubsub:a.getGoldlogVal("aplus_pubsub"),pubsubType:"hjlj"},_=new s;_.create(d),_.wrap(g,function(){d.context.status="complete",d.context.method=t.method,r.doPubMsg(["mw_change_hjlj",d.context]),n&amp;&amp;n.fn_after_record&amp;&amp;o.each(n.fn_after_record,function(t){t(window.goldlog)}),"function"==typeof l&amp;&amp;l()})()}},function(t,e,n){"use strict";function o(){}var a=n(24),r=n(22),i=n(23),s=n(3),u=n(11);o.prototype.create=function(t){for(var e in t)"undefined"==typeof this[e]&amp;&amp;(this[e]=t[e]);return this},o.prototype.pubsubInfo=function(t,e){try{t&amp;&amp;t.pubsub&amp;&amp;t.pubsub.publish("mw_change_"+t.pubsubType,t.context,e)}catch(t){}},o.prototype.calledList=[],o.prototype.setCalledList=function(t){a.indexof(this.calledList,t)===-1&amp;&amp;this.calledList.push(t)},o.prototype.resetCalledList=function(){this.calledList=[]},o.prototype.wrap=function(t,e){var n=this,o=this.context||{},c=o.compose||{},l=c.maxTimeout||1e4;return function(o){var c,p=t.length,g=0,f=0,d=function(){if(n.pubsubInfo(n,t[g]),g===p)return o="done",n.resetCalledList(),"function"==typeof e&amp;&amp;e.call(n,o),void clearTimeout(c);if(a.indexof(n.calledList,g)===-1){if(n.setCalledList(g),!t[g]||"function"!=typeof t[g][0])return;try{o=t[g][0].call(n,o,function(){g++,f=1,clearTimeout(c),d(g)})}catch(e){s.do_tracker_jserror({message:e?e.message:"compose middleware error",error:encodeURIComponent(e.stack),filename:t[g][1]})}}var _="number"==typeof o;if("pause"===o||_){f=0;var h=_?o:l,m=t[g]?t[g][1]:"";c=r.sleep(h,function(){if(0===f){var t="jump the middleware about "+m+", because waiting timeout maxTimeout = "+h+"ms!";i.logger({msg:t});var e=window.goldlog_queue||(window.goldlog_queue=[]);e.push({action:"goldlog._aplus_cplugin_m.do_tracker_browser_support",arguments:[{msg:t,spmab:goldlog.spm_ab,page:location.href,etag:n.context?JSON.stringify(n.context.etag):"",cna:document.cookie?u.getCookie("cna"):""}]}),o=null,g++,d(g)}})}else"done"===o?(g=p,d(g)):(g++,d(g))};return n.calledList&amp;&amp;n.calledList.length&gt;0&amp;&amp;n.resetCalledList(),d(g)}},t.exports=o},function(t,e,n){"use strict";var o=n(24);t.exports=function(){return{init:function(t){this.opts=t,t&amp;&amp;"object"==typeof t.middleware&amp;&amp;t.middleware.length&gt;0?this.middleware=t.middleware:this.middleware=[],this.plugins_name=[]},pubsubInfo:function(t,e){try{var n=t.pubsub;n&amp;&amp;n.publish("plugins_change_"+t.pubsubType,e)}catch(t){}},checkPluginLoader:function(t,e){var n=!0;if("object"==typeof e.enable&amp;&amp;"function"==typeof e.enable.isEnable?n=e.enable.isEnable(e.name):"boolean"==typeof e.enable&amp;&amp;(n=!!e.enable),!n)return!1;if(n&amp;&amp;e.deps&amp;&amp;e.deps.length&gt;0)for(var a=0;a&lt;e.deps.length;a++)if(o.indexof(this.plugins_name,e.deps[a])===-1)return!1;return!0},run:function(t){t||(t=0);var e=this,n=this.middleware,o=this.opts||{},a=o.plugins;if(a&amp;&amp;"object"==typeof a&amp;&amp;a.length&gt;0){var r=a[t];if(this.checkPluginLoader(a,r)&amp;&amp;(this.plugins_name.push(r.name),n.push([function(t,n){e.pubsubInfo(this,r);var a=new r.path;return a.init({context:this.context,config:o.config}),a.run(t,n)},r.name])),t++,a[t])return this.run(t)}else window.console&amp;&amp;console.log("aplus plugins "+JSON.stringify(a)+" must be object of array!");return n}}}},function(t,e,n){"use strict";function o(){var t="true"===l.disablePvid;try{var e=goldlog.getMetaInfo("aplus-disable-pvid")+"";"true"===e?t=!0:"false"===e&amp;&amp;(t=!1)}catch(t){}return t}function a(t){function e(t){var e="0123456789abcdefhijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ",n="0123456789abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ";return 1==t?e.substr(Math.floor(60*Math.random()),1):2==t?n.substr(Math.floor(60*Math.random()),1):"0"}for(var n,o="",a="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",r=!1;o.length&lt;t;)n=a.substr(Math.floor(62*Math.random()),1),!r&amp;&amp;o.length&lt;=2&amp;&amp;("g"==n.toLowerCase()||"l"==n.toLowerCase())&amp;&amp;(0===o.length&amp;&amp;"g"==n.toLowerCase()?Math.random()&lt;.5&amp;&amp;(n=e(1),r=!0):1==o.length&amp;&amp;"l"==n.toLowerCase()&amp;&amp;"g"==o.charAt(0).toLowerCase()&amp;&amp;(n=e(2),r=!0)),o+=n;return o}function r(t,e,n){return t?u.hash(encodeURIComponent(t)).substr(0,e):n}function i(){var t=a(8),e=t.substr(0,4),n=t.substr(0,6);return[r(location.href,4,e),r(document.title,4,e),n].join("")}function s(){var t=goldlog.pvid;return goldlog.pvid=i(),c.doPubMsg(["pvidChange",{pre_pvid:t,pvid:goldlog.pvid}]),c.doCachePubs(["pvidChange",{pre_pvid:t,pvid:goldlog.pvid}]),o()?"":goldlog.pvid}var u=n(93),c=n(37),l=n(4);e.isDisablePvid=o,e.makePVId=s,e.getPvId=function(){return o()?"":goldlog.pvid}},function(t,e){"use strict";var n=1315423911;e.hash=function(t,e){var o,a,r=e||n;for(o=t.length-1;o&gt;=0;o--)a=t.charCodeAt(o),r^=(r&lt;&lt;5)+a+(r&gt;&gt;2);var i=(2147483647&amp;r).toString(16);return i}},function(t,e,n){"use strict";var o=n(9),a=n(25),r=n(37),i=n(23),s=n(90),u=n(91),c=n(4),l=function(){};l.prototype.run=function(t,e,n){var l=new u;l.init({middleware:[],config:t,plugins:c.plugins_pv});var p=l.run(),g=new c.context;g.userdata=e,g.logger=i.logger;var f={context:g,pubsub:a.getGoldlogVal("aplus_pubsub"),pubsubType:"pv"},d=new s;d.create(f),d.wrap(p,function(){var e=f.context.can_to_sendpv||{};f.context.status="YES"===e.flag?"complete":"skip",f.context.method=t.method||"GET",r.doPubMsg(["mw_change_pv",f.context]),n&amp;&amp;n.fn_after_record&amp;&amp;o.each(n.fn_after_pv,function(e){e(window.goldlog,t)})})()},e.SendPV=l},function(t,e,n){"use strict";var o=n(9),a=n(25),r=n(37),i=n(23),s=n(90),u=n(91),c=n(4),l=function(){};l.prototype.run=function(t,e,n,l){var p=new u;p.init({middleware:[],config:t,plugins:c.plugins_prepv});var g=p.run(),f=new c.context_prepv;f.userdata=e,f.logger=i.logger;var d={context:f,pubsub:a.getGoldlogVal("aplus_pubsub"),pubsubType:"prepv"},_=new s;_.create(d),_.wrap(g,function(){d.context.status="complete",r.doPubMsg(["mw_change_prepv",d.context]),n&amp;&amp;n.fn_after_record&amp;&amp;o.each(n.fn_after_pv,function(e){e(window.goldlog,t)}),a.setGoldlogVal("prepv_context",f),"function"==typeof l&amp;&amp;l()})()},e.SendPrePV=l},function(t,e,n){"use strict";!function(){var t=window.goldlog||(window.goldlog={}),e=n(97);t.aplus_pubsub||(t.aplus_pubsub=e.create())}()},function(t,e,n){"use strict";function o(t){if("function"!=typeof t)throw new TypeError(t+" is not a function");return t}var a=n(85),r=function(t){for(var e=t.length,n=new Array(e-1),o=1;o&lt;e;o++)n[o-1]=t[o];return n},i=a.extend({create:function(t){var e=new this;for(var n in t)e[n]=t[n];return e.handlers=[],e.pubs={},e},setHandlers:function(t){this.handlers=t},subscribe:function(t,e){o(e);var n=this,a=n.pubs||{},r=a[t]||[];if(r)for(var i=0;i&lt;r.length;i++){var s=r[i]();e.apply(n,s)}var u=n.handlers||[];return t in u||(u[t]=[]),u[t].push(e),n.setHandlers(u),n},subscribeOnce:function(t,e){o(e);var n,a=this;return this.subscribe.call(this,t,n=function(){a.unsubscribe.call(a,t,n);var o=Array.prototype.slice.call(arguments);e.apply(a,o)}),this},unsubscribe:function(t,e){o(e);var n=this.handlers[t];if(!n)return this;if("object"==typeof n&amp;&amp;n.length&gt;0){for(var a=0;a&lt;n.length;a++){var r=e.toString(),i=n[a].toString();r===i&amp;&amp;n.splice(a,1)}this.handlers[t]=n}else delete this.handlers[t];return this},publish:function(t){var e=r(arguments),n=this.handlers||[],o=n[t]?n[t].length:0;if(o&gt;0)for(var a=0;a&lt;o;a++){var i=n[t][a];i&amp;&amp;"function"==typeof i&amp;&amp;i.apply(this,e)}return this},cachePubs:function(t){var e=this.pubs||{},n=r(arguments);e[t]||(e[t]=[]),e[t].push(function(){return n})}});t.exports=i},function(t,e,n){"use strict";var o=n(40),a=n(37),r=n(53),i=n(4);e.init=function(){i.initLoad.init_watchGoldlogQueue("metaQueue"),n(99)(function(){var t=goldlog._$||{},e=navigator.userAgent;e.match(/AliApp\(([A-Z\-]+)\/([\d\.]+)\)/i)&amp;&amp;(t.is_ali_app=!0),i.utilPvid.makePVId();var s=n(51);t.spm=s,t.is_WindVane=o.is_WindVane;var u=t.meta_info;s.init(goldlog,u,function(){i.initLoad.init_watchGoldlogQueue();var t=n(4).spmException,e=t.is_exception;e||n(101);var o,r="complete";o=["aplusReady",r],a.doPubMsg(o),a.doCachePubs(o)}),goldlog.beforeSendPV(function(e,n){if(t.page_url=location.href,t.page_referrer=r.getRefer(),n.is_auto&amp;&amp;"1"===u["aplus-manual-pv"])return!1}),goldlog.afterSendPV(function(){window.g_SPM&amp;&amp;(g_SPM._current_spm="")}),i.is_auto_pv+""=="true"&amp;&amp;goldlog.sendPV({is_auto:!0}),i.initLoad.run(),i.beforeUnload.run()})}},function(t,e,n){"use strict";var o=n(37);t.exports=function(t){var e=n(100).AplusInit,a=new e;a.run({},function(e){o.doPubMsg(["aplusInitContext",e]),o.doCachePubs(["aplusInitContext",e]),"function"==typeof t&amp;&amp;t()})}},function(t,e,n){"use strict";var o=n(25),a=n(23),r=n(90),i=n(91),s=n(4),u=function(){};u.prototype.run=function(t,e){var n=new i;n.init({middleware:[],config:t,plugins:s.aplus_init});var u=n.run(),c=new s.context;c.logger=a.logger;var l={context:c,pubsub:o.getGoldlogVal("aplus_pubsub"),pubsubType:"aplusinit"},p=new r;p.create(l),p.wrap(u,function(){"function"==typeof e&amp;&amp;e(l.context)})()},e.AplusInit=u},function(t,e,n){"use strict";!function(){var t,e=n(9),o=n(25),a=n(102),r=function(){t=!0;var n=window.g_SPM||{};e.isFunction(n.getParam)||e.isFunction(n.spm)||a.run()},i=window.goldlog||(window.goldlog={});i.aplus_pubsub&amp;&amp;"function"==typeof i.aplus_pubsub.publish&amp;&amp;i.aplus_pubsub.subscribe("goldlogReady",function(e){"complete"!==e||t||r()});var s=0,u=function(){if(!t){var e=o.getGoldlogVal("_$")||{};"complete"===e.status?r():s&lt;50&amp;&amp;(++s,setTimeout(function(){u()},200))}};u()}()},function(t,e,n){"use strict";var o=n(30),a=n(25),r=n(103),i=n(107),s=n(108),u=n(109),c=n(110);e.run=function(){var t=a.getGoldlogVal("_$")||{},e=t.meta_info,n=e["aplus-touch"],l={isTouchEnabled:o.isTouch()||"1"===n||"tap"===n,isTerminal:t.is_terminal||/WindVane/i.test(navigator.userAgent)};window.g_SPM={spm_d_for_ad:{},resetModule:r.spm_resetModule,anchorBeacon:r.spm_spmAnchorChk,getParam:r.spm_getSPMParam,spm:r.spm_forwap},i.run(l),s.run(l),u.run(l),c.run(l)}},function(t,e,n){"use strict";function o(t){if(t&amp;&amp;1===t.nodeType){s.tryToRemoveAttribute(t,"data-spm-max-idx"),s.tryToRemoveAttribute(t,"data-auto-spmd-max-idx");for(var e=u.nodeListToArray(t.getElementsByTagName("a")),n=u.nodeListToArray(t.getElementsByTagName("area")),o=e.concat(n),a=0;a&lt;o.length;a++)s.tryToRemoveAttribute(o[a],l)}}function a(t,e){var n=s.tryToGetAttribute(t,l),o="0";if(n&amp;&amp;c.spm_isSPMAnchorIdMatch(n))c.spm_anchorEnsureSPMId_inHref(t,n,e);else{var a=c.spm_spmGetParentSPMId(t.parentNode);if(o=a.spm_c,!o)return void c.spm_dealNoneSPMLink(t,e);c.spm_initSPMModule(a.el,o,e),c.spm_initSPMModule(a.el,o,e,!0)}}function r(t){var e,n=t.tagName;"A"!==n&amp;&amp;"AREA"!==n?e=c.spm_getParamForAD(t):(a(t,!0),e=s.tryToGetAttribute(t,l)),e||(e="0.0.0.0");var o=goldlog.getPvId();4===e.split(".").length&amp;&amp;o&amp;&amp;(e+="."+o),"A"!==n&amp;&amp;"AREA"!==n&amp;&amp;s.tryToSetAttribute(t,l,e),e=e.split(".");var r={a:e[0],b:e[1],c:e[2],d:e[3]};return e[4]&amp;&amp;(r.e=e[4]),r}function i(t,e){var n=r(t),o=[n.a,n.b,n.c,n.d];return e&amp;&amp;n.e&amp;&amp;o.push(n.e),o.join(".")}var s=n(27),u=n(18),c=n(104),l="data-spm-anchor-id";e.spm_resetModule=o,e.spm_spmAnchorChk=a,e.spm_getSPMParam=r,e.spm_forwap=i},function(t,e,n){"use strict";function o(t){for(var e,n="data-spm-ab-max-idx",o={},a="";t&amp;&amp;t.tagName!=T&amp;&amp;t.tagName!=x;){if(!a&amp;&amp;(a=v.tryToGetAttribute(t,"data-spm-ab"))){e=parseInt(v.tryToGetAttribute(t,n))||0,o.a_spm_ab=a,o.ab_idx=++e,t.setAttribute(n,e);break}if(v.tryToGetAttribute(t,"data-spm"))break;t=t.parentNode}return o}function a(){var t=b.getGoldlogVal("_$")||{},e=t.spm.data;return[e.a,e.b].join(".")}function r(t){var e=a(),n=t.split(".");return n[0]+"."+n[1]==e}function i(t,e){if(!goldlog.isUT4Aplus||"UT4Aplus"!==goldlog.getMetaInfo("aplus-toUT")){if(t&amp;&amp;/&amp;?\bspm=[^&amp;#]*/.test(t)&amp;&amp;(t=t.replace(/&amp;?\bspm=[^&amp;#]*/g,"").replace(/&amp;{2,}/g,"&amp;").replace(/\?&amp;/,"?").replace(/\?$/,"")),!e)return t;var n,o,a,r,i,s,u,c="&amp;";t.indexOf("#")!==-1&amp;&amp;(a=t.split("#"),t=a.shift(),o=a.join("#")),r=t.split("?"),i=r.length-1,a=r[0].split("//"),a=a[a.length-1].split("/"),s=a.length&gt;1?a.pop():"",i&gt;0&amp;&amp;(n=r.pop(),t=r.join("?")),n&amp;&amp;i&gt;1&amp;&amp;n.indexOf("&amp;")==-1&amp;&amp;n.indexOf("%")!==-1&amp;&amp;(c="%26");var l="";if(t=t+"?spm="+l+e+(n?c+n:"")+(o?"#"+o:""),u=h.isContain(s,".")?s.split(".").pop().toLowerCase():""){if({PNG:1,jpg:1,jpeg:1,gif:1,bmp:1,swf:1}.hasOwnProperty(u))return 0;!n&amp;&amp;i&lt;=1&amp;&amp;(o||{htm:1,HTML:1,php:1,aspx:1,shtml:1,xhtml:1}.hasOwnProperty(u)||(t+="&amp;file="+s))}return t}}function s(t,e){if(!goldlog.isUT4Aplus||"UT4Aplus"!==goldlog.getMetaInfo("aplus-toUT")){var n,o=t.innerHTML;o&amp;&amp;o.indexOf("&lt;")==-1&amp;&amp;(n=document.createElement("b"),n.style.display="none",t.appendChild(n)),t.href=e,n&amp;&amp;t.removeChild(n)}}function u(t,e,n){if(!/^0\.0\.?/.test(e)){var o=y.tryToGetHref(t),r=a(),u=w.is_ignore_spm(t);if(u){var c=_.param2obj(o);if(c.spm&amp;&amp;c.spm.split)for(var l=c.spm.split("."),p=e.split("."),g=0;g&lt;3&amp;&amp;p[g]===l[g];g++)2===g&amp;&amp;l[3]&amp;&amp;(e=c.spm)}t.setAttribute("data-spm-anchor-id",e);var f=goldlog.getPvId();f&amp;&amp;(e+="."+f);var d="0.0";(f||r&amp;&amp;r!=d)&amp;&amp;(u||n||(o=i(o,e))&amp;&amp;s(t,o))}}function c(t){var e=v.tryToGetAttribute(t,P),n=m.parseSemicolonContent(e)||{};return n}function l(t){var e,n=b.getGoldlogVal("_$")||{},o=n.spm.data;return"0"==o.a&amp;&amp;"0"==o.b?e="0":(e=v.tryToGetAttribute(t,j),e&amp;&amp;e.match(/^d\w+$/)||(e="")),e}function p(t,e){for(var n=[],o=m.nodeListToArray(t.getElementsByTagName("a")),a=m.nodeListToArray(t.getElementsByTagName("area")),r=o.concat(a),i=0;i&lt;r.length;i++){for(var s=!1,u=r[i],c=r[i];(u=u.parentNode)&amp;&amp;u!=t;)if(v.tryToGetAttribute(u,j)){s=!0;break}if(!s){var l=v.tryToGetAttribute(c,S);e||"t"===l?e&amp;&amp;"t"===l&amp;&amp;n.push(c):n.push(c)}}return n}function g(t){for(var e,n=t;t&amp;&amp;t.tagName!==T&amp;&amp;t.tagName!==x&amp;&amp;t.getAttribute;){var o=t.getAttribute(j);if(o){e=o,n=t;break}if(!(t=t.parentNode))break}return e&amp;&amp;!/^[\w\-\.\/]+$/.test(e)&amp;&amp;(e="0"),{spm_c:e,el:n}}function f(t,e){var n=parent!==self;if(!n&amp;&amp;e)return[t,e].join(".");if(t&amp;&amp;e)return t+".i"+e;var o=window.g_SPM||(window.g_SPM={}),a=o.spm_d_for_ad||{};return"number"==typeof a[t]?a[t]++:a[t]=0,o.spm_d_for_ad=a,t+".i"+a[t]}function d(t){var e;return t&amp;&amp;(e=t.match(/&amp;?\bspm=([^&amp;#]*)/))?e[1]:""}var _=n(17),h=n(9),m=n(18),v=n(27),b=n(25),y=n(105),w=n(106),x="BODY",T="HTML",j="data-spm",P="data-spm-click",S="data-auto-spmd",A="data-spm-anchor-id";e.getGlobalSPMId=a,e.spm_isSPMAnchorIdMatch=r,e.spm_updateHrefWithSPMId=i,e.spm_writeHref=s,e.spm_anchorEnsureSPMId_inHref=u,e.getElDataSpm=c,e.spm_getAnchor4thId_spm_d=l,e.spm_getModuleLinks=p,e.spm_spmGetParentSPMId=g,e.get_spm_for_ad=f,e.spm_getParamForAD=function(t){var e=v.tryToGetAttribute(t,A);if(!e){var n=a(),o=t.parentNode;if(!o)return"";var r=c(t)||{},i=r.locaid||"",s=t.getAttribute(j)||i,u=g(o),l=u.spm_c||0;l&amp;&amp;l.indexOf(".")!==-1&amp;&amp;(l=l.split("."),l=l[l.length-1]),e=f(n+"."+l,s)}return e},e.spm_initSPMModule=function(t,e,n,i){var s;if(e=e||t.getAttribute("data-spm")||""){var g=p(t,i);if(0!==g.length){var f=e.split("."),d=h.isStartWith(e,"110")&amp;&amp;3==f.length;d&amp;&amp;(s=f[2],f[2]="w"+(s||"0"),e=f.join("."));var _=a();if(_&amp;&amp;_.match(/^[\w\-\*]+(\.[\w\-\*\/]+)?$/))if(h.isContain(e,".")){if(!h.isStartWith(e,_)){var m=_.split(".");f=e.split(".");for(var b=0;b&lt;m.length;b++)f[b]=m[b];e=f.join(".")}}else h.isContain(_,".")||(_+=".0"),e=_+"."+e;if(e.match&amp;&amp;e.match(/^[\w\-\*]+\.[\w\-\*\/]+\.[\w\-\*\/]+$/)){for(var w="data-auto-spmd-max-idx",x="data-spm-max-idx",T=i?w:x,j=parseInt(v.tryToGetAttribute(t,T))||0,S=0;S&lt;g.length;S++){var k=g[S],U=y.tryToGetHref(k),E=v.tryToGetAttribute(k,P);if(i||U||E){d&amp;&amp;k.setAttribute("data-spm-wangpu-module-id",s);var M=k.getAttribute(A);if(M&amp;&amp;r(M))u(k,M,n);else{var I,C,N=o(k.parentNode);N.a_spm_ab?(C=N.a_spm_ab,I=N.ab_idx):(C=void 0,j++,I=j);var V,O=c(k)||{},G=O.locaid||"";G?V=G:(V=l(k)||I,i&amp;&amp;(V="at"+((h.isNumber(V)?1e3:"")+V))),M=C?e+"-"+C+"."+V:e+"."+V,u(k,M,n)}}}t.setAttribute(T,j)}}}},e.spm_dealNoneSPMLink=function(t,e){var n=goldlog.getMetaInfo("aplus-getspmcd"),o=a(),r=y.tryToGetHref(t),i=d(r),c=null,p=o&amp;&amp;2==o.split(".").length;if(p){var g;return"function"==typeof n&amp;&amp;(g=n(t,null,o)),c=g&amp;&amp;"0"!==g.spm_c?[o,g.spm_c,g.spm_d]:[o,0,l(t)||0],void u(t,c.join("."),e)}r&amp;&amp;i&amp;&amp;(r=r.replace(/&amp;?\bspm=[^&amp;#]*/g,"").replace(/&amp;{2,}/g,"&amp;").replace(/\?&amp;/,"?").replace(/\?$/,"").replace(/\?#/,"#"),s(t,r))}},function(t,e,n){"use strict";var o=n(19);e.tryToGetHref=function(t){var e;try{e=o.trim(t.getAttribute("href",2))}catch(t){}return e||""}},function(t,e,n){"use strict";function o(t){return!!t&amp;&amp;!!t.match(/^[^\?]*\balipay\.(?:com|net)\b/i)}function a(t){return!!t&amp;&amp;!!t.match(/^[^\?]*\balipay\.(?:com|net)\/.*\?.*\bsign=.*/i)}function r(t){var e=location.href;return t&amp;&amp;e.split("#")[0]===t.split("#")[0]}function i(t){for(var e;(t=t.parentNode)&amp;&amp;"BODY"!==t.tagName;)if(e=u.tryToGetAttribute(t,f))return e;return""}function s(t){for(var e=["mclick.simba.taobao.com","click.simba.taobao.com","click.tanx.com","click.mz.simba.taobao.com","click.tz.simba.taobao.com","redirect.simba.taobao.com","rdstat.tanx.com","stat.simba.taobao.com","s.click.taobao.com"],n=0;n&lt;e.length;n++)if(t.indexOf(e[n])!==-1)return!0;return!1}var u=n(27),c=n(9),l=n(105),p=n(25),g=n(21),f="data-spm-protocol";e.is_ignore_spm=function(t){var e=p.getGoldlogVal("_$")||{},n=e.meta_info||{},d=l.tryToGetHref(t),_=i(t),h=u.tryToGetAttribute(t,f),m="i"===(h||_||n.spm_protocol);if(!d||s(d))return!0;var v=r(d)||g.isStartWithProtocol(d.toLowerCase()),b=o(d)||a(d),y=v||b;return!(m||!c.isStartWith(d,"#")&amp;&amp;!y)||m}},function(t,e,n){"use strict";function o(t,e,n){var o=u.parseSemicolonContent(e,{},!0),a=o.gostr||"",r=o.locaid||"",g=t.getAttribute("data-spm")||r,f="CLK",d=o.gokey||"",_=p.spm_getSPMParam(t),h=[_.a,_.b,_.c,g].join("."),m=a+"."+h;0!==m.indexOf("/")&amp;&amp;(m="/"+m);var v=[],b=["gostr","locaid","gmkey","gokey","spm-cnt","cna"];for(var y in o)o.hasOwnProperty(y)&amp;&amp;c.indexof(b,y)===-1&amp;&amp;v.push(y+"="+o[y]);v.push("_g_et="+n),v.push("autosend=1"),d&amp;&amp;v.length&gt;0&amp;&amp;(d+="&amp;"),d+=v.length&gt;0?v.join("&amp;"):"",goldlog&amp;&amp;s.isFunction(goldlog.recordUdata)?goldlog.recordUdata(m,f,d,"GET",function(){}):l.logger({msg:"goldlog.recordUdata is not function!"}),i.tryToSetAttribute(t,"data-spm-anchor-id",h)}function a(t,e){var n=e;window.g_SPM&amp;&amp;(g_SPM._current_spm=p.spm_getSPMParam(e));for(var a;e&amp;&amp;"HTML"!==e.tagName;){a=i.tryToGetAttribute(e,"data-spm-click");{if(a){o(e,a,"mousedown"===t.type?t.type:"tap");break}e=e.parentNode}}if(!a){var r=g.getGlobalSPMId(),s=goldlog.getMetaInfo("aplus-getspmcd");"function"==typeof s&amp;&amp;s(n,t,r)}}var r=n(79),i=n(27),s=n(9),u=n(18),c=n(24),l=n(23),p=n(103),g=n(104);e.run=function(t){t&amp;&amp;t.isTouchEnabled?r.on(document,"tap",a):r.on(document,"mousedown",a)}},function(t,e,n){"use strict";function o(){for(var t=document.getElementsByTagName("iframe"),e=0;e&lt;t.length;e++){var n=t[e],o=r.tryToGetAttribute(n,"data-spm-src");if(!n.src&amp;&amp;o){var a=s.spm_getSPMParam(n);if(a){var u=[a.a,a.b,a.c,a.d];a.e&amp;&amp;u.push(a.e),a=u.join("."),n.src=i.spm_updateHrefWithSPMId(o,a)}else n.src=o}}}function a(){function t(){e++,e&gt;10&amp;&amp;(n=3e3),o(),setTimeout(t,n)}var e=0,n=500;t()}var r=n(27),i=n(104),s=n(103);e.run=function(t){t&amp;&amp;!t.isTerminal&amp;&amp;a()}},function(t,e,n){"use strict";function o(t,e){for(var n,o=window;e&amp;&amp;(n=e.tagName);){if("A"===n||"AREA"===n){r.spm_spmAnchorChk(e,!1);var a=o.g_SPM||(o.g_SPM={}),i=a._current_spm=r.spm_getSPMParam(e),s=[];try{s=[i.a,i.b,i.c,i.d];var u=i.e||goldlog.pvid||"";u&amp;&amp;s.push(u)}catch(t){}break}if("BODY"==n||"HTML"==n)break;e=e.parentNode}}var a=n(79),r=n(103);e.run=function(t){var e=document;t&amp;&amp;t.isTouchEnabled?a.on(e,"tapSpm",o):(a.on(e,"mousedown",o),a.on(e,"keydown",o))}},function(t,e,n){"use strict";function o(t,e){if(e||(e=p),p.evaluate)return e.evaluate(t,p,null,9,null).singleNodeValue;for(var n,a=t.split("/");!n&amp;&amp;a.length&gt;0;)n=a.shift();var r,i=/^.+?\[@id='(.+?)']$/i,s=/^(.+?)\[(\d+)]$/i;return(r=n.match(i))?e=e.getElementById(r[1]):(r=n.match(s))&amp;&amp;(e=e.getElementsByTagName(r[1])[parseInt(r[2])-1]),e?0===a.length?e:o(a.join("/"),e):null}function a(){var t={};for(var e in l)if(l.hasOwnProperty(e)){var n=o(e);if(n){t[e]=1;var a=l[e],r="A"===n.tagName?a.spmd:a.spmc;s.tryToSetAttribute(n,"data-spm",r||"")}}for(var i in t)t.hasOwnProperty(i)&amp;&amp;delete l[i]}function r(){if(!c&amp;&amp;g.spmData){c=!0;var t=g.spmData.data;if(t&amp;&amp;i.isArray(t)){for(var e=0;e&lt;t.length;e++){var n=t[e],o=n.xpath;o=o.replace(/^id\('(.+?)'\)(.*)/g,"//*[@id='$1']$2"),l[o]={spmc:n.spmc,spmd:n.spmd}}a()}}}var i=n(9),s=n(27),u=n(79),c=!1,l={},p=document,g=window;e.wh_updateXPathElements=a,e.init_wh=r,e.run=function(){u.DOMReady(function(){r()})}},function(t,e,n){"use strict";var o=n(53),a=n(54),r=n(37),i=n(42),s=n(4),u=n(26),c=u.getInfo(),l="complete";e.initGoldlog=function(t){var e=window.goldlog||(window.goldlog={}),n=s.goldlog_path.run.create();e._ready_time=(new Date).getTime();for(var u in n)e[u]=n[u];var p=/TB\-PD/i.test(navigator.userAgent),g=e._$=e._$||{};return g.meta_info=c,g.is_terminal="aplus_wap"===s.script_name||p||"1"==c["aplus-terminal"],g.send_pv_count=0,g.status=l,g.script_name=s.script_name,g.spm={data:{}},g.page_referrer=o.getRefer(),g.pageLoadTime=(new Date).getTime(),e.lver=s.lver,e.nameStorage=a.nameStorage,i.haveNativeFlagInUA(),r.doPubMsg(["goldlogReady",l]),r.doCachePubs(["goldlogReady",l]),
t.init(),e}}]);/*! 2020-03-17 20:01:00 v8.13.5 */
!function(t){function e(n){if(r[n])return r[n].exports;var a=r[n]={exports:{},id:n,loaded:!1};return t[n].call(a.exports,a,a.exports,e),a.loaded=!0,a.exports}var r={};return e.m=t,e.c=r,e.p="",e(0)}([function(t,e){"use strict";!function(){function t(t,e,r){t[_]((h?"on":"")+e,function(t){t=t||s.event;var e=t.target||t.srcElement;r(t,e)},!1)}function e(){return/&amp;?\bspm=[^&amp;#]*/.test(location.href)?location.href.match(/&amp;?\bspm=[^&amp;#]*/gi)[0].split("=")[1]:""}function r(t,e){if(t&amp;&amp;/&amp;?\bspm=[^&amp;#]*/.test(t)&amp;&amp;(t=t.replace(/&amp;?\bspm=[^&amp;#]*/g,"").replace(/&amp;{2,}/g,"&amp;").replace(/\?&amp;/,"?").replace(/\?$/,"")),!e)return t;var r,n,a,i,o,c,p,s="&amp;";if(t.indexOf("#")!=-1&amp;&amp;(a=t.split("#"),t=a.shift(),n=a.join("#")),i=t.split("?"),o=i.length-1,a=i[0].split("//"),a=a[a.length-1].split("/"),c=a.length&gt;1?a.pop():"",o&gt;0&amp;&amp;(r=i.pop(),t=i.join("?")),r&amp;&amp;o&gt;1&amp;&amp;r.indexOf("&amp;")==-1&amp;&amp;r.indexOf("%")!=-1&amp;&amp;(s="%26"),t=t+"?spm="+e+(r?s+r:"")+(n?"#"+n:""),p=c.indexOf(".")&gt;-1?c.split(".").pop().toLowerCase():""){if({PNG:1,jpg:1,jpeg:1,gif:1,bmp:1,swf:1}.hasOwnProperty(p))return 0;!r&amp;&amp;o&lt;=1&amp;&amp;(n||{htm:1,HTML:1,php:1}.hasOwnProperty(p)||(t+="&amp;file="+c))}return t}function n(t){function e(t){return t=t.replace(/refpos[=(%3D)]\w*/gi,c).replace(i,"%3D"+n+"%26"+a.replace("=","%3D")).replace(o,n),a.length&gt;0&amp;&amp;(t+="&amp;"+a),t}var r=window.location.href,n=r.match(/mm_\d{0,24}_\d{0,24}_\d{0,24}/i),a=r.match(/[&amp;\?](pvid=[^&amp;]*)/i),i=new RegExp("%3Dmm_\\d+_\\d+_\\d+","ig"),o=new RegExp("mm_\\d+_\\d+_\\d+","ig");a=a&amp;&amp;a[1]?a[1]:"";var c=r.match(/(refpos=(\d{0,24}_\d{0,24}_\d{0,24})?(,[a-z]+)?)(,[a-z]+)?/i);return c=c&amp;&amp;c[0]?c[0]:"",n?(n=n[0],e(t)):t}function a(e){var r=s.KISSY;r?r.ready(e):s.jQuery?jQuery(m).ready(e):"complete"===m.readyState?e():t(s,"load",e)}function i(t,e){return t&amp;&amp;t.getAttribute?t.getAttribute(e)||"":""}function o(t){if(t){var e,r=g.length;for(e=0;e&lt;r;e++)if(t.indexOf(g[e])&gt;-1)return!0;return!1}}function c(t,e){if(t&amp;&amp;/&amp;?\bspm=[^&amp;#]*/.test(t)&amp;&amp;(t=t.replace(/&amp;?\bspm=[^&amp;#]*/g,"").replace(/&amp;{2,}/g,"&amp;").replace(/\?&amp;/,"?").replace(/\?$/,"")),!e)return t;var r,n,a,i,o,c,p,s="&amp;";if(t.indexOf("#")!=-1&amp;&amp;(a=t.split("#"),t=a.shift(),n=a.join("#")),i=t.split("?"),o=i.length-1,a=i[0].split("//"),a=a[a.length-1].split("/"),c=a.length&gt;1?a.pop():"",o&gt;0&amp;&amp;(r=i.pop(),t=i.join("?")),r&amp;&amp;o&gt;1&amp;&amp;r.indexOf("&amp;")==-1&amp;&amp;r.indexOf("%")!=-1&amp;&amp;(s="%26"),t=t+"?spm="+e+(r?s+r:"")+(n?"#"+n:""),p=c.indexOf(".")&gt;-1?c.split(".").pop().toLowerCase():""){if({PNG:1,jpg:1,jpeg:1,gif:1,bmp:1,swf:1}.hasOwnProperty(p))return 0;!r&amp;&amp;o&lt;=1&amp;&amp;(n||{htm:1,HTML:1,shtml:1,php:1}.hasOwnProperty(p)||(t+="&amp;__file="+c))}return t}function p(t){if(o(t.href)){var r=i(t,u);if(!r){var n=l()(t),a=[n.a,n.b,n.c,n.d].join(".");n.e&amp;&amp;(n+="."+n.e),d&amp;&amp;(a=[n.a||"0",n.b||"0",n.c||"0",n.d||"0"].join("."),a=(e()||"0.0.0.0.0")+"_"+a),t.href=c(t.href,a),t.setAttribute(u,a)}}}var s=window,m=document;if(1!==s.aplus_spmact){s.aplus_spmact=1;var f=function(){return{a:0,b:0,c:0,d:0,e:0}},l=function(){return s.g_SPM&amp;&amp;s.g_SPM.getParam?s.g_SPM.getParam:f},d=!0;try{d=self.location!=top.location}catch(t){}var u="data-spm-act-id",g=["mclick.simba.taobao.com","click.simba.taobao.com","click.tanx.com","click.mz.simba.taobao.com","click.tz.simba.taobao.com","redirect.simba.taobao.com","rdstat.tanx.com","stat.simba.taobao.com","s.click.taobao.com"],h=!!m.attachEvent,b="attachEvent",v="addEventListener",_=h?b:v;t(m,"mousedown",function(t,e){for(var r,n=0;e&amp;&amp;(r=e.tagName)&amp;&amp;n&lt;5;){if("A"==r||"AREA"==r){p(e);break}if("BODY"==r||"HTML"==r)break;e=e.parentNode,n++}}),a(function(){for(var t,a,o=document.getElementsByTagName("iframe"),c=0;c&lt;o.length;c++){t=i(o[c],"mmsrc"),a=i(o[c],"mmworked");var p=l()(o[c]),s=[p.a||"0",p.b||"0",p.c||"0",p.d||"0",p.e||"0"].join(".");t&amp;&amp;!a?(d&amp;&amp;(s=[p.a||"0",p.b||"0",p.c||"0",p.d||"0"].join("."),s=e()+"_"+s),o[c].src=r(n(t),s),o[c].setAttribute("mmworked","mmworked")):o[c].setAttribute(u,s)}})}}()}]);</script><script charset="utf-8" src="https://g.alicdn.com/mui/code-tracker/3.1.2/??code-tracker.js?t=1.js" async=""/><script charset="utf-8" src="https://g.alicdn.com/kissy/k/1.4.14/??base-min.js,attribute-min.js,node-min.js,anim-min.js,anim/base-min.js,promise-min.js,anim/timer-min.js,anim/transition-min.js,io-min.js?t=1.js" async=""/><script charset="utf-8" src="https://g.alicdn.com/mui/??datalazyload/3.0.2/index.js?t=1.js" async=""/><script charset="utf-8" src="https://g.alicdn.com/tm/list/2.25.17/??mods/srp/grid.js,mods/srp/cells/pin.js,mods/crumb/crumb.js,mods/attr/attr.js,atp2nav.js,mods/related/related.js,mods/filter/filter.js,widgets/city-codes.js,mods/srp/cells/sku.js,mods/p4p/p4p.js,core.js,init.js,pages/list.js,atp-v2.js,rn.js,filter.js,other.js?t=1.js" async=""/><script src="//uaction.alicdn.com/js/ua.js?1585288800000" async=""/><script charset="utf-8" src="https://g.alicdn.com/kissy/k/1.4.14/??dom/base-min.js,event-min.js,event/dom/base-min.js,event/base-min.js,event/dom/shake-min.js,event/dom/focusin-min.js,event/custom-min.js,cookie-min.js?t=1.js" async=""/><meta charset="gbk"/><meta name="spm-id" content="a220m.1000858"/><meta name="renderer" content="webkit"/><meta name="description" content="智能手机,品类齐全，欢迎选购！"/><meta name="viewport" content="width=device-width"/><link rel="dns-prefetch" href="//g.alicdn.com"/><link rel="dns-prefetch" href="//assets.alicdn.com"/><link rel="dns-prefetch" href="//img.alicdn.com"/><link rel="dns-prefetch" href="//smc.tmall.com"/><link rel="dns-prefetch" href="//www.tmall.com"/><link rel="dns-prefetch" href="//bar.tmall.com"/><link rel="dns-prefetch" href="//pcookie.tmall.com"/><link rel="dns-prefetch" href="//log.mmstat.com"/><link rel="dns-prefetch" href="//ac.mmstat.com"/><link rel="dns-prefetch" href="//ac.atpanel.com"/><link rel="dns-prefetch" href="//amos.alicdn.com"/>  <title>智能手机-天猫Tmall.com-理想生活上天猫</title>
  <link rel="shortcut icon" href="//img.alicdn.com/tfs/TB1XlF3RpXXXXc6XXXXXXXXXXXX-16-16.PNG" type="image/x-icon"/>
  <script>
 window.g_config = window.g_config || {};
 window.g_config.devId = "pc";
 window.g_config.headerVersion = '1.0.0';
           window.g_config.loadModulesLater = true;
 window.g_config.sl = 'vm';
 </script>
        
<script>(function(){var a=[['sysId','list'],['appId',2003],['appName','tmallsearch'],['pageType','list'],['pageId','list'],['version','2.0'],['startTime',+new Date],['ap_mods',{poc:[0.001],jstracker:[0.001]}]];window.g_config=window.g_config||{};for(var i=0,l=a.length;i&lt;l;i++){window.g_config[a[i][0]]=a[i][1]}})();window.g_config.ueId = 187;
window.g_config.activity_rt='158;161;203;299;328;455;529;534;537;572;601;604;608;612';
window.g_config.cat_rt='1512';
window.g_config.u2iApi = '';
window.g_config.ueUrl = '//feedback.taobao.com/pc/feedbacks?productId=338&amp;source=Web';

window._ap=window._ap||[];_ap.push(["_poc", "_trackCustom", "tpl", "sync"]);window.onerror=function(){_ap.push(["jstracker","_trackCustom","msg="+(arguments[0]?encodeURIComponent(arguments[0]):"")+"&amp;file="+(arguments[1]?encodeURIComponent(arguments[1]):"")+"&amp;line="+(arguments[2]?encodeURIComponent(arguments[2]):"")])};</script>


  <!-- globalmodule version: 3.0.85 -->
<link rel="stylesheet" href="//g.alicdn.com/??mui/global/3.0.31/global.css"/>
<script src="//g.alicdn.com/??kissy/k/1.4.14/seed-min.js,mui/seed/1.4.8/seed.js,mui/globalmodule/3.0.85/seed.js,mui/btscfg-g/3.0.0/index.js,mui/bucket/3.0.4/index.js,mui/globalmodule/3.0.85/global-mod-pc.js,mui/globalmodule/3.0.85/global-mod.js,mui/global/3.0.31/global-pc.js,mui/global/3.0.31/global.js,tm/list/2.25.17/mui-seed.js,tm/list/2.25.17/seed.js"/>
<script src="//g.alicdn.com/secdev/pointman/js/index.js" app="tmall"/>
<script>
   TB.environment.isApp = true;
   TB.environment.passCookie = true;
 </script>
  <link rel="stylesheet" href="//g.alicdn.com/mui/3c-base/4.0.20/pc/??logo/common.css,index.css"/>



<link rel="stylesheet" href="//g.alicdn.com/??tm/list/2.25.18/mods/srp/cells/pin.css,tm/list/2.25.18/pages/layout.css,tm/list/2.25.18/pages/base.css,tm/list/2.25.18/pages/mui.css,tm/list/2.25.18/mods/error/error.css,tm/list/2.25.18/mods/tmall-rec.css,tm/list/2.25.18/mods/crumb/crumb.css,tm/list/2.25.18/mods/attr/attr.css,tm/list/2.25.18/mods/related/related.css,tm/list/2.25.18/mods/filter/filter.css,tm/list/2.25.18/mods/filter/couponfilter.css,tm/list/2.25.18/mods/locData.css,tm/list/2.25.18/mods/srp/grid.css,tm/list/2.25.18/pages/bts.css"/>
 <script>
window.g_config=window.g_config||{};
window.g_config.SearchbarFeature={
          };
</script><script type="text/javascript">
</script><script src="//g.alicdn.com/secdev/sufei_data/3.8.7/index.js" id="aplus-sufei"/><script src="//g.alicdn.com/secdev/nsv/1.0.72/ns_d_83_3_f.js"/></head>



<body class="pg"><script id="tb-beacon-aplus" src="//g.alicdn.com/alilog/mlog/aplus_v2.js" exparams="category=2&amp;userid=&amp;at_type=search&amp;at_bucketid=sbucket%5f0&amp;at_mall_pro_re=10001&amp;aplus&amp;at_rn=032b31e22ca2541dc3d92935018d8b3e&amp;yunid=&amp;e34d5139635ae&amp;asid=AQAAAACDoH1eYEsiGQAAAADw5CdgSN3SXA=="/><script>
with(document)with(body)with(insertBefore(createElement("script"),firstChild))setAttribute("exparams","category=2&amp;userid=&amp;at_type=search&amp;at_bucketid=sbucket%5f0&amp;at_mall_pro_re=10001&amp;aplus&amp;at_rn=032b31e22ca2541dc3d92935018d8b3e&amp;yunid=&amp;e34d5139635ae&amp;asid=AQAAAACDoH1eYEsiGQAAAADw5CdgSN3SXA==",id="tb-beacon-aplus",src=(location&gt;"https"?"//g":"//g")+".alicdn.com/alilog/mlog/aplus_v2.js")
</script>

 <script>(function(){function n(i,r,o){var a,c,f,u,l=i;if(!i)return l;if(i[e])return o[i[e]].destination;if('object'==typeof i){var s=i.constructor;t.inArray(s,[Boolean,String,Number,Date,RegExp])?l=new s(i.valueOf()):(a=t.isArray(i))?l=r?t.filter(i,r):i.concat():(c=t.isPlainObject(i))&amp;&amp;(l={}),i[e]=u=t.guid('c'),o[u]={destination:l,input:i}}if(a)for(var v=0;v&lt;l.length;v++)l[v]=n(l[v],r,o);else if(c)for(f in i)f===e||r&amp;&amp;r.call(i,i[f],f,i)===FALSE||(l[f]=n(i[f],r,o));return l}var t=KISSY,e='__~ks_cloned';t.clone=function(i,r){var o={},a=n(i,r,o);return t.each(o,function(n){if(n=n.input,n[e])try{delete n[e]}catch(t){n[e]=void 0}}),o=null,a}})();(function(e){var t=window,a=document,r=a.body;t.LIST=t.LIST||{};LIST.msg=e.EventTarget?e.mix(LIST.msg||{},e.EventTarget,1):LIST.msg||{};LIST.data=LIST.data||{};t.g_config=e.merge(t.g_config||{},{v:'1.0',t:'20130804',aldt:20130228,closePoc:0||0,poc:{mods:1||0},webp:1||0,toggle:{smc:1||0,pin:1||0,brandDynamic:0||0,filter:1||0},tmpFlag:1||0});e.use('dom,event,ua',function(e,i,n,o){var s=o.ie,c=s&lt;9,l=o.core=='webkit',u='ontouchstart'in a;!LIST.msg.on&amp;&amp;(LIST.msg=e.mix(LIST.msg,n.Target));s&amp;&amp;i.addClass(r,'ie ie'+s);i[u?'removeClass':'addClass']('HTML','no-touch');t.g_config.vps=l?[1190+17+3,1583+17]:[1190,1583];LIST.updateView=function(e,a){a=a||0;if(!e){t.g_config.view=0}else if(a==t.g_config.vps.length||e&lt;t.g_config.vps[a]){t.g_config.view=a}else{this.updateView(e,++a)}};LIST.changeView=function(e){var a=i.viewportWidth(),n=t.g_config.view||0;if(e)a-=17;this.updateView(a);if(c){i.removeClass(r,'w'+n);i.addClass(r,'w'+t.g_config.view)}return a};LIST.changeView(1);n.on(t,'resize',function(){var e=t.g_config.view||0,a=LIST.changeView();if(t.g_config.view!==e){LIST.msg.fire('viewchange',{vp:a,view:t.g_config.view})}})});t._ap=t._ap||[];t.TMPoc={add:function(e){},trackCT:function(e,a){},trackCV:function(e,a){}}})(KISSY);</script><style>#mallSearch label{visibility:hidden;}.product .productPrice .proPrice_zk{height:20px!important;}.product .productStatus span{white-space:nowrap;}i.f-ico-triangle-mb{border-top: 4px solid #806F66;border-width: 3px\9; /* IE8~9 */*border-width: 3px;right:6px\9;*right:6px;top: 12px;}.minisite.mv6{margin-bottom:10px}.minisite.mv6 .m-story{margin-top:12px;padding:0;height:auto;max-height: 38px;_height: expression(function(el){if(/msie 6/i.test(navigator.userAgent))el.style.height = (el.scrollHeight &gt; 38) ? '38px' : 'auto';}(this));}.minisite.mv6 .m-brand .mb-logo span{font-size: 14px;display: inline-block;line-height: 20px;overflow: hidden;color: #000;word-break: break-all;max-height: 36px;_height: expression(function(el){if(/msie 6/i.test(navigator.userAgent))el.style.height = (el.scrollHeight &gt; 36) ? '36px' : 'auto';}(this));}.crumb{padding-bottom:8px;margin-bottom:0;}#mallNav{margin-bottom:0}.productImg{_height:100%!important;}.bts-70 .miniAttrs .forMultiple{background: #F3F3F3;}.navAttrsForm{*z-index:11}</style>   <input type="hidden" value="e34d5139635ae" id="J_TbToken"/>
  <div class="page">
<!--dingtianB begin -->

<!--dingtianB end -->
          <div id="mallPage" class=" mallist tmall-3c page-not-market ">
  <style>
button {
  border-radius: 0;
}
</style>
<!--from fragment-->
<div id="site-nav" data-spm="a2226mz" role="navigation">
    <div id="sn-bg">
        <div class="sn-bg-right">
        </div>
    </div>
    <div id="sn-bd">
        <b class="sn-edge"/>
        <div class="sn-container">
            <p class="sn-back-home"><i class="mui-global-iconfont">󰄫</i><a href="//www.tmall.com/">天猫首页</a></p><p id="login-info" class="sn-login-info"><em>喵，欢迎来天猫</em><a class="sn-login" href="//login.tmall.com/?redirectURL=https%3A%2F%2Flist.tmall.com%2Fsearch_product.htm%3Fq%3D%25E6%2599%25BA%25E8%2583%25BD%25E6%2589%258B%25E6%259C%25BA%26type%3Dp%26style%3D%26cat%3Dall%26vmarket%3D" target="_top">请登录</a><a class="sn-register" href="//register.tmall.com/" target="_top">免费注册</a></p>
            <ul class="sn-quick-menu">
                <li class="sn-mytaobao menu-item j_MyTaobao">
                    <div class="sn-menu">
                        <a class="menu-hd" href="//i.taobao.com/my_taobao.htm" target="_top" rel="nofollow" tabindex="0" aria-haspopup="true" aria-expanded="false">我的淘宝<b/></a>
                        <div class="menu-bd" role="menu" aria-hidden="true" id="menu-533">
                            <div class="menu-bd-panel" id="myTaobaoPanel">
                                <a href="//trade.taobao.com/trade/itemlist/list_bought_items.htm?t=20110530" target="_top" rel="nofollow">已买到的宝贝</a>
                                <a href="//trade.taobao.com/trade/itemlist/list_sold_items.htm?t=20110530" target="_top" rel="nofollow">已卖出的宝贝</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="sn-seller-center hidden j_SellerCenter">
                    <a target="_top" href="//mai.taobao.com/seller_admin.htm">商家中心</a>
                </li>
                <li class="sn-cart"><i class="mui-global-iconfont">󰅈</i>
                    <a class="sn-cart-link" href="//cart.tmall.com/cart/myCart.htm?from=btop" target="_top" rel="nofollow">购物车
                    </a>
                </li>
                <li class="sn-favorite menu-item">
                    <div class="sn-menu">
                        <a class="menu-hd" href="//shoucang.taobao.com/shop_collect_list.htm?scjjc=c1" target="_top" rel="nofollow" tabindex="0" aria-haspopup="true" aria-expanded="false">收藏夹<b/></a>

                        <div class="menu-bd" role="menu" aria-hidden="true" id="menu-535">
                            <div class="menu-bd-panel">
                                <a href="//shoucang.taobao.com/item_collect.htm" target="_top" rel="nofollow">收藏的宝贝</a>
                                <a href="//shoucang.taobao.com/shop_collect_list.htm" target="_top" rel="nofollow">收藏的店铺</a>
                            </div>
                        </div>
                    </div>
                </li>
                <li class="sn-separator"/>
                <li class="sn-mobile">
                    <i class="mui-global-iconfont">㑈</i>
                    <a title="天猫无线" target="_top" class="sn-mobile-link" href="//pages.tmall.com/wow/portal/act/app-download?scm=1027.1.1.1">手机版</a>
                </li>
                <li class="sn-home">
                    <a href="//www.taobao.com/">淘宝网</a>
                </li>
                <li class="sn-seller menu-item">
                    <div class="sn-menu J_DirectPromo">
                        <a class="menu-hd" href="//mai.taobao.com" target="_top">商家支持<b/></a>
                        <div class="menu-bd sn-seller-lazy">
                        </div>
                    </div>
                </li>
                <li class="sn-sitemap">
                    <div class="sn-menu">
                        <h3 class="menu-hd"><i class="mui-global-iconfont"></i><span>网站导航</span><b/></h3>
                        <div class="menu-bd sn-sitemap-lazy sn-sitemap-bd" data-spm="a2228l4">
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>

  <div id="header" class="mallChn header-list-app" data-spm="a2226n0">
 <div class="headerLayout">
 <div class="headerCon ">
 <h1 id="mallLogo">
  <span class="mlogo">
   <a class="logo-3c" href="//3c.tmall.com/?scm=1238.1.2.1" title="天猫电器城-3c.tmall.com"><s/>天猫电器城-3c.tmall.com</a>
   </span>
  <span class="slogo">
 <a href="//3c.tmall.com/">电器城</a>
 </span>
</h1>

 <div class="header-extra">
   <div class="header-banner">
 


 </div>
       <div id="mallSearch" class="mall-search">
 <form name="searchTop" action="//list.tmall.com/search_product.htm" class="mallSearch-form clearfix" target="_top">
 <fieldset>
 <legend>天猫搜索</legend>
 <div class="mallSearch-input clearfix">
 <label for="mq">搜索 天猫 商品/品牌/店铺</label>

 <div class="s-combobox">
 <div class="s-combobox-input-wrap">
   <input type="text" name="q" accesskey="s" autocomplete="off" x-webkit-speech="" x-webkit-grammar="builtin:search" value="智能手机" id="mq" data-bts=""/>
   </div>
 </div>
 <button type="submit">搜索<s/>
 </button>
 <input id="J_Type" type="hidden" name="type" value="p"/>
 <input id="J_MallSearchStyle" type="hidden" name="style" value=""/>
 <input id="J_Cat" type="hidden" name="cat" value="all"/>
 <input type="hidden" name="vmarket" value="72"/>
   </div>
 </fieldset>
 </form>
  <ul class="relKeyTop" data-spm="a220m.1000858.1000723" data-atp="{loc},{q},,,spu-key,5,key-top-s,"><li><a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%BB%AA%CE%AA%CA%D6%BB%FA">华为手机</a></li><li><a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%D0%A1%C3%D7%CA%D6%BB%FA">小米手机</a></li><li><a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=vivo%CA%D6%BB%FA">vivo手机</a></li><li><a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%C0%CF%C4%EA%CA%D6%BB%FA">老年手机</a></li><li><a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%BA%EC%C3%D7">红米</a></li><li><a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%D6%C7%C4%DC%D2%F4%CF%E4">智能音箱</a></li><li><a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%CA%D6%BB%FA%C6%BB%B9%FB">手机苹果</a></li><li><a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%D3%CE%CF%B7%CA%D6%BB%FA">游戏手机</a></li></ul></div>
   </div>
 </div>
 </div>
 </div>
  

<div id="J_navRow" data-fixed="off" class="c3-navrow-global" data-module-id="100">
    <div class="c3-navrow-container" data-spm="a2226c3nav">
    <div class="c3-navrow-con">
       <ul class="c3-navrow-ul clearfix">
       	
       	
       	<li class="nav-item-index">
       		<a href="//3c.tmall.com/?acm=lb-zebra-155904-807029.1003.4.767290&amp;scm=1003.4.lb-zebra-155904-807029.OTHER_14592974949620_767290" data-code="index">电器城首页</a>
       	</li>
       	
       	
       	
       	
       	
       	
       	
       	
       	
       	<li class="nav-item-shouji">
       		<a href="//shouji.tmall.com?acm=lb-zebra-155904-807029.1003.4.767290&amp;scm=1003.4.lb-zebra-155904-807029.OTHER_14592967254716_767290" data-code="shouji">手机馆</a>
       	</li>
       	
       	
       	
       	<li class="nav-item-suningyigou">
       		<a href="//suning.tmall.com?acm=lb-zebra-155904-807029.1003.4.767290&amp;scm=1003.4.lb-zebra-155904-807029.OTHER_14592944169808_767290" data-code="suningyigou">苏宁易购</a>
       	</li>
       	
       	
      </ul>
       <s class="c3-nav-indicator"/>
    </div>
    <div class="c3-navrow-sub"> 
    
    
    <a href="//www.tmall.com/wow/tmall-3c/act/serve?acm=lb-zebra-155904-807028.1003.8.767393&amp;scm=1003.8.lb-zebra-155904-807028.ITEM_14592985267191_767393" data-code="servertable" class="nav-sub-servertable">电器城服务台</a>
    
    
    </div>  
</div>
</div>
<div id="J_navPlaceholder" class="c3-navrow-pholder"/>

  <div id="content">



     

            


   


       



     
                        
 <div class="main      bts-61 ">
       
    <div class="crumb" id="J_crumbs">
 <div class="crumbCon">
  <div class="crumbSlide" id="J_CrumbSlide">
<a title="上一页" class="crumbSlide-prev" id="J_CrumbSlidePrev" style="visibility: hidden;">&lt;</a>
 <i class="crumbSlide-prev-shadow"/>
 <div class="crumbClip">
 <ul class="crumbSlide-con clearfix" id="J_CrumbSlideCon" data-atp="{loc},{i},,,,{t},rightnav,">
   <li>
   <a class="crumbStrong" href="/search_product.htm?search_condition=7&amp;style=g&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;from=sn_1_rightnav#J_crumbs" data-i="cat" data-t="3">全部</a>
   <i class="crumbArrow">&gt;</i>
 </li>
                        
         <li class="crumbSearch">
 <form action="" id="J_CrumbSearchForm">
     <label class="crumbSearch-label" for="J_CrumbSearchInuput">
 <input type="text" name="q" value="智能手机" class="crumbSearch-input" id="J_CrumbSearchInuput" aria-label="搜索关键词"/>
 </label>
 <input type="submit" value="" id="J_CrumbSearchBtn" class="crumbSearch-btn" onclick="atpanelFun(',secondsearch,,,,20,rightnav,')" aria-label="搜索"/>
   <input type="hidden" name="sort" value="s"/><input type="hidden" name="style" value="g"/>          
       
       
       
   </form>
 </li>
   </ul>
 </div>
 <i class="crumbSlide-next-shadow"/>
 <a title="下一页" class="crumbSlide-next" id="J_CrumbSlideNext" style="visibility: hidden;">&gt;</a>
 </div>
<p class="crumbTitle j_ResultsNumber" xd="10001">共<span> 86345</span>件相关商品</p>
     </div>
</div>  
   
   <div id="J_SuggestTipWrap">



</div>

       






<form id="J_NavAttrsForm" class="navAttrsForm">  <a id="J_AttrsTrigger" class="attrsTrigger" href="javascript:;" atpanel=",,,,selectbutton,20,selectbutton,">筛选<i class="list-font i-expand">󰀂</i><i class="list-font i-collapse">󰀃</i><s class="attrsTrigger-new"/></a>




<div class="attrs j_NavAttrs" style="display:block">
   <div class="brandAttr j_nav_brand" data-spm="a220m.1000858.1000720">
<div class="j_Brand attr">
 <div class="attrKey">品牌</div>
 <div class="attrValues showLogo">
  <div class="j_BrandSearch av-search clearfix">
 <input type="text" value="" placeholder="搜索 品牌名称" style="color: rgb(191, 191, 191);"/>
 </div>
  <ul class="av-collapse row-2" data-atp="{loc},{brand},,,{f},4,{c},">
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=11813&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="Huawei/华为">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1Z.mzyMmTBuNjy1XbXXaMrVXa" alt="Huawei/华为"/>
 Huawei/华为
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=3506680&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="Xiaomi/小米">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1wh2sj.z1gK0jSZLewu29kVXa.PNG" alt="Xiaomi/小米"/>
 Xiaomi/小米
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=590022244&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="honor/荣耀">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1gR9vsyrpK1RjSZFhXXXSdXXa" alt="honor/荣耀"/>
 honor/荣耀
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=91621&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="vivo">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1QkxTCXzqK1RjSZFCXXbbxVXa" alt="vivo"/>
 vivo
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=28247&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="OPPO">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1UWloLzTpK1RjSZKPXXa3UpXa" alt="OPPO"/>
 OPPO
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=81156&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="Samsung/三星">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1lsMhLFXXXXb1XFXXSutbFXXX.jpg" alt="Samsung/三星"/>
 Samsung/三星
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=30111&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="Apple/苹果">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1vDvUKpXXXXaKXFXXSutbFXXX.jpg" alt="Apple/苹果"/>
 Apple/苹果
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=2965867101&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="realme">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1V2A.wFP7gK0jSZFjwu35aXXa.PNG" alt="realme"/>
 realme
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=582926107&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="小辣椒">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1DGSMKXXXXXbaXpXXSutbFXXX.jpg" alt="小辣椒"/>
 小辣椒
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=11542&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="Coolpad/酷派">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1.OyOKXXXXXX.XVXXSutbFXXX.jpg" alt="Coolpad/酷派"/>
 Coolpad/酷派
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=11208&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="ZTE/中兴">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1s45OJFXXXXcIXFXXSutbFXXX.jpg" alt="ZTE/中兴"/>
 ZTE/中兴
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=11119&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="Lenovo/联想">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1QGlkSVXXXXcLXpXXXXXXXXXX" alt="Lenovo/联想"/>
 Lenovo/联想
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=60679&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="纽曼">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB19jR7LpXXXXccXFXXxKNpFXXX.jpeg" alt="纽曼"/>
 纽曼
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=26487995&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="DOOV/朵唯">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1c8kCNpXXXXaxXFXXSutbFXXX.jpg" alt="DOOV/朵唯"/>
 DOOV/朵唯
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=84416&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="K-Touch/天语">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB17mRRFVXXXXcKaXXXXXXXXXXX" alt="K-Touch/天语"/>
 K-Touch/天语
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=10246&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="Philips/飞利浦">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1hkk0RXXXXXXgXXXXXXXXXXXX" alt="Philips/飞利浦"/>
 Philips/飞利浦
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=10123&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="Motorola/摩托罗拉">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB1z.kyJFXXXXcsXXXXSutbFXXX.jpg" alt="Motorola/摩托罗拉"/>
 Motorola/摩托罗拉
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=1749033532&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="创星（手机）">
 <img style="" src="//img.alicdn.com/bao/uploaded/TB12kRcicrI8KJjy0FhXXbfnpXa" alt="创星（手机）"/>
 创星（手机）
 </a>
 </li>
  <li>
 <a data-f="spu-brand-qp" data-c="brand-qp" href="?brand=1945600210&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_brand-qp&amp;industryCatId=all#J_crumbs" title="皓轩">
 皓轩
 </a>
 </li>
  </ul>
  <div class="av-options">
 <a class="j_Multiple avo-multiple" href="javascript:;" atpanel="0,brand-multi,,,,20,brand,">多选<i/></a>
  <a style="visibility: visible; display: inline;" class="j_More avo-more ui-more-drop-l" href="javascript:;" data-url="//list.tmall.com/ajax/allBrandShowForGaiBan.htm?q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;industryCatId=all&amp;userIDNum=&amp;tracknick=" atpanel="0,20000_more,,,spu-brand,20,brand,">
  更多
 <i class="ui-more-drop-l-arrow"/>
 </a>
 </div>
 <div class="av-btns">
 <a class="j_SubmitBtn ui-btn-s-primary ui-btn-disable" href="javascript:;" atpanel="0,brand-multi,,,,20,brand,">确定</a>
 <a class="j_CancelBtn ui-btn-s" href="javascript:;">取消</a>
 </div>
  </div>
</div>
</div>
      <div class="cateAttrs j_nav_cat" data-spm="a220m.1000858.1000721">
              <div class="j_Cate attr">
<div class="attrKey">分类</div>
<div class="attrValues">
<ul class="av-collapse" data-atp="{loc},{cat},,,{f},3,{c}," style="height: auto;">
<li>
 <a title="手机" data-f="spu-cat-qp" data-c="cat-qp" href="?cat=50024400&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_cat-qp&amp;industryCatId=all#J_crumbs">
 <b>手机</b>
 </a>
 </li>
<li>
 <a title="手机" data-f="spu-cat-qp" data-c="cat-qp" href="?cat=56946005&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;from=sn_1_cat-qp&amp;industryCatId=all#J_crumbs">
 <b>手机</b>
 </a>
 </li>

</ul>
</div>
</div>
</div>
      <div class="attrs-border"/>
    </div>
<input type="hidden" name="sort" value="s"/><input type="hidden" name="style" value="g"/><input type="hidden" name="q" value="智能手机"/><input type="hidden" name="brand" value=""/>
<input type="hidden" name="prop" value=""/>

</form>      <div id="J_RelSearch">


  <p class="relKeyRec relKeyHide" data-spm="a220m.1000858.1000723" data-atp="{loc},{q},,,spu-key,5,key-top-s,">
 <span>您是不是想找</span>
     
 
            <a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%BB%AA%CE%AA%CA%D6%BB%FA">华为手机</a>
                <a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%D0%A1%C3%D7%CA%D6%BB%FA">小米手机</a>
                <a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=vivo%CA%D6%BB%FA">vivo手机</a>
                <a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%C0%CF%C4%EA%CA%D6%BB%FA">老年手机</a>
                <a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%BA%EC%C3%D7">红米</a>
                <a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%D6%C7%C4%DC%D2%F4%CF%E4">智能音箱</a>
                <a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%CA%D6%BB%FA%C6%BB%B9%FB">手机苹果</a>
                <a href="/search_product.htm?&amp;from=rs_1_key-top-s&amp;q=%D3%CE%CF%B7%CA%D6%BB%FA">游戏手机</a>
                               </p>
</div>
        

<div class="filter clearfix" id="J_Filter" data-spm="a220m.1000858.1000724">
   <a class="fSort fSort-cur" href="?q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;industryCatId=all#J_Filter" title="点击后恢复默认排序" atpanel="11,zong_he,,,spu-sort,20,sort,">综合<i class="f-ico-arrow-d"/></a>
       <a class="fSort" href="?q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=rq&amp;style=g&amp;industryCatId=all#J_Filter" title="点击后按人气从高到低" atpanel="10,ren_qi,,,spu-sort,20,sort,">人气<i class="f-ico-arrow-d"/></a>
 
<!--Test   -->
<!--Test s  -->
  <a class="fSort" href="?q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=new&amp;style=g&amp;industryCatId=all#J_Filter" atpanel="3,new,,,,20,sort,,">新品<i class="f-ico-arrow-d"/></a>
 
<a class="fSort" href="?q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=d&amp;style=g&amp;industryCatId=all#J_Filter" title="点击后按月销量从高到低" atpanel="7,week_sale,,,spu-sort,20,sort,">销量<i class="f-ico-arrow-d"/></a>



<a class="fSort" href="?q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=p&amp;style=g&amp;industryCatId=all#J_Filter" title="点击后按价格升序" atpanel="9,price_ascending,,,spu-sort,20,sort,">价格<i class="f-ico-triangle-mt"/><i class="f-ico-triangle-mb"/></a>
      <div class="fArea fDestArea" id="J_FDestArea">
<s class="fA-label">收货地：</s>
<b class="fA-text">杭州 </b>
 <i class="f-ico-triangle-rb"/>
 <div class="fA-list">
 <div class="fAl-hd clearfix">
 <span>选择收货城市</span>
 </div>

 

<ul class="fAl-loc" data-atp="2,{text},,,spu-toloc,20,toloc,">
 <li><a href="" code="110100">北京</a></li>
 <li><a href="" code="120100">天津</a></li>
 <li><a href="" code="310100">上海</a></li>
 <li><a href="" code="500100">重庆</a></li>
 <li class="fAll-cities"/>
</ul>
<ul class="fAl-loc" data-atp="2,{text},,,spu-toloc,20,toloc,">
 <li><a href="" code="130000">河北</a></li>
 <li><a href="" code="140000">山西</a></li>
 <li><a href="" code="150000">内蒙古</a></li>
 <li><a href="" code="210000">辽宁</a></li>
 <li><a href="" code="220000">吉林</a></li>
 <li><a href="" code="230000">黑龙江</a></li>
 <li class="fAll-cities"/>
 <li><a href="" code="320000">江苏</a></li>
 <li><a href="" code="330000">浙江</a></li>
 <li><a href="" code="340000">安徽</a></li>
 <li><a href="" code="350000">福建</a></li>
 <li><a href="" code="360000">江西</a></li>
 <li><a href="" code="370000">山东</a></li>
 <li class="fAll-cities"/>
 <li><a href="" code="410000">河南</a></li>
 <li><a href="" code="420000">湖北</a></li>
 <li><a href="" code="430000">湖南</a></li>
 <li><a href="" code="440000">广东</a></li>
 <li><a href="" code="450000">广西</a></li>
 <li><a href="" code="460000">海南</a></li>
 <li class="fAll-cities"/>
 <li><a href="" code="510000">四川</a></li>
 <li><a href="" code="520000">贵州</a></li>
 <li><a href="" code="530000">云南</a></li>
 <li><a href="" code="540000">西藏</a></li>
 <li><a href="" code="610000">陕西</a></li>
 <li><a href="" code="620000">甘肃</a></li>
 <li class="fAll-cities"/>
 <li><a href="" code="630000">青海</a></li>
 <li><a href="" code="640000">宁夏</a></li>
 <li><a href="" code="650000">新疆</a></li>
 <li><a href="" code="710000">台湾</a></li>
 <li><a href="" code="810000">香港</a></li>
 <li><a href="" code="820000">澳门</a></li>
 <li class="fAll-cities"/>
</ul>

<form id="J_DestAreaForm">
<input type="hidden" value="" name="sarea_code"/>
<input type="hidden" value="智能手机" name="q"/>            <input type="hidden" name="sort" value="s"/><input type="hidden" name="style" value="g"/>                                                       <input name="shopType" type="hidden" value="any"/>       <input name="sceneq" type="hidden" value=""/>     </form>
 </div>
</div>
  <form id="J_FForm">
<div class="fPrice" id="J_FPrice">
 <div class="fP-box">
 <b class="fPb-item">
 <i class="ui-price-plain">¥</i>
 <input type="text" name="start_price" autocomplete="off" maxlength="6" value="" class="j_FPInput" aria-label="最低价" placeholder="请输入最低价"/>
 </b>
 <i class="fPb-split"/>
 <b class="fPb-item">
 <i class="ui-price-plain">¥</i>
 <input type="text" name="end_price" autocomplete="off" value="" maxlength="6" class="j_FPInput" aria-label="最高价" placeholder="请输入最高价"/>
 </b>
 </div>

 <div class="fP-expand">
 <a class="ui-btn-s" id="J_FPCancel">清空</a>
 <a class="ui-btn-s-primary" id="J_FPEnter" atpanel=",,,,spu-fprice,20,fprice,">确定</a>
 </div>
</div><div class="fMenu" id="J_FMenu">
   <div class="fM-con">
<a href="javascript:;" hidefocus="true" class="j_FMcExpand ui-more-drop-l">更多<i class="ui-more-drop-l-arrow"/></a>




  


<label><input type="checkbox" name="post_fee" value="-1" atpanel="1,post_fee-1,,,spu-fservice,20,fservice," aria-label="包邮"/>包邮</label>

<label><input type="checkbox" name="miaosha" value="1" atpanel="2,miaosha-1,,,spu-fservice,20,fservice," aria-label="折扣"/>折扣</label>

<label><input type="checkbox" name="combo" value="1" atpanel="3,combo-1,,,spu-fservice,20,fservice," aria-label="搭配减价"/>搭配减价</label>
<label><input type="checkbox" name="filter_mj" value="1" atpanel="7,filter_mj-1,,,spu-fservice,20,fservice," aria-label="满就减"/>满就减</label>
<label><input type="checkbox" name="support_cod" value="1" atpanel="8,support_cod-1,,,spu-fservice,20,fservice," aria-label="货到付款"/>货到付款</label>
<label><input type="checkbox" name="normal_cod" value="1" atpanel="8,normal_cod-1,,,spu-fservice,20,fservice," aria-label="通用排序"/>通用排序</label>
 </div>
</div>

  <input type="hidden" name="search_condition" value="48"/>           <input type="hidden" name="sort" value="s"/><input type="hidden" name="style" value="g"/>   <input name="q" type="hidden" value="智能手机"/>             <input name="shopType" type="hidden" value="any"/>         <input name="sceneq" type="hidden" value=""/>  

       





</form>

  <a href=" ?q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=w&amp;industryCatId=all#J_Filter" class="fType-w " atpanel=",w,,,,20,filter,">店铺<i class="fTw-ico"/></a>
     <a href="javascript:; " class="fType-g fType-cur" atpanel=",g,,,,20,filter,">大图<i class="fTg-ico"/></a>
   
  <p class="ui-page-s">
<b class="ui-page-s-len">1/80</b>
<b class="ui-page-s-prev" title="上一页">&lt;</b>
<a href="?s=60&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;industryCatId=all&amp;type=pc#J_Filter" class="ui-page-s-next" atpanel="1,pagedn,,,,20,fservice," title="下一页">&gt;</a>
</p></div><div id="J_FilterPlaceholder" style="height: 54px; display: none;"/>

           <div id="J_Combo" class="combo">
</div>

      
<div class="view  view-noCom" id="J_ItemList" data-spm="a220m.1000858.1000725" data-area="杭州" data-atp-a="{p},{id},,,spu,1,spu,{user_id}" data-atp-b="{p},{id},,,spu,2,spu,{user_id}">




 
    

<div class="product  " data-id="606307762219" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=606307762219&amp;skuId=4309474780759&amp;standard=1&amp;user_id=2838892713&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="1-10">
<img src="//img.alicdn.com/bao/uploaded/i4/TB1IFWxl5_1gK0jSZFq59.paXXa_112746.jpg"/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:43832396" class="proThumb-img " data-index="1:1">
 <img atpanel="1-1,606307762219,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1fXCVv1H2gK0jSZJnL6ST1FXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:524272456" class="proThumb-img " data-index="1:2">
 <img atpanel="1-2,606307762219,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1b2yTvYH1gK0jSZFwL6U7aXXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:614390616" class="proThumb-img " data-index="1:3">
 <img atpanel="1-3,606307762219,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1zVojvebviK0jSZFNL6SApXXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:6503543" class="proThumb-img " data-index="1:4">
 <img atpanel="1-4,606307762219,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1kWKUvYY1gK0jSZTEL6RDQVXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:8988157" class="proThumb-img " data-index="1:5">
 <img atpanel="1-5,606307762219,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB13JWVvYj1gK0jSZFuL6UrHpXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:986234554" class="proThumb-img " data-index="1:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/TB1wfqPv4D1gK0jSZFsL6TldVXa_30x30.jpg" atpanel="1-6,606307762219,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">

<em title="6399.00"><b>¥</b>6399.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=606307762219&amp;skuId=4309474780759&amp;standard=1&amp;user_id=2838892713&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="HUAWEI Huawei Mate 30 Pro 5G" data-p="1-11">HUAWEI Huawei Mate 30 Pro 5G</a>

</div>
<div class="productShop" data-atp="b!1-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2838892713&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
华为官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1398186641&amp;suid=5af4a045cb7c8fda9d86340047faf827&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="1-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>5.1万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="606307762219" data-nick="华为官方旗舰店" data-tnick="华为官方旗舰店" data-display="inline" data-atp="a!1-2,,,,,,,2838892713"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="605258110430" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=605258110430&amp;skuId=4266775277489&amp;standard=1&amp;user_id=2616970884&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="2-10">
<img src="//img.alicdn.com/bao/uploaded/i1/1917047079/O1CN01wmhZr022AEJB9610K_!!2-item_pic.PNG"/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28320" class="proThumb-img " data-index="2:1">
 <img atpanel="2-1,605258110430,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/1917047079/O1CN01pC06ke22AEJ8IgFIr_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:28324" class="proThumb-img " data-index="2:2">
 <img atpanel="2-2,605258110430,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/1917047079/O1CN019UAAq022AEJ9AY42h_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:28326" class="proThumb-img " data-index="2:3">
 <img atpanel="2-3,605258110430,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i2/1917047079/O1CN01KyppMw22AEJAcsczH_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:28329" class="proThumb-img " data-index="2:4">
 <img atpanel="2-4,605258110430,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i2/1917047079/O1CN01PP4wv322AEJ9gGIkc_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:28335" class="proThumb-img " data-index="2:5">
 <img atpanel="2-5,605258110430,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/1917047079/O1CN01uqE1Gm22AEJ9snzam_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:28341" class="proThumb-img " data-index="2:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i1/1917047079/O1CN01aeFudA22AEJ9sojJP_!!2-item_pic.png_30x30.jpg" atpanel="2-6,605258110430,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">
<a class="tag"><img src="http://tmallfans.cn-hangzhou.oss-pub.aliyun-inc.com/pifu/files/110363/20180912020202.png"/></a>

<em title="5999.00"><b>¥</b>5999.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=605258110430&amp;skuId=4266775277489&amp;standard=1&amp;user_id=2616970884&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Apple/苹果 iPhone 11" data-p="2-11">Apple/苹果 iPhone 11</a>

</div>
<div class="productShop" data-atp="b!2-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2616970884&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
苏宁易购官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1340548940&amp;suid=613234933671e1b9a65e6b9b646fdf9d&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="2-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>15万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="605258110430" data-nick="苏宁易购官方旗舰店" data-tnick="苏宁易购官方旗舰店" data-display="inline" data-atp="a!2-2,,,,,,,2616970884"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="605468103182" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=605468103182&amp;skuId=4266777221080&amp;standard=1&amp;user_id=2616970884&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="3-10">
<img src="//img.alicdn.com/bao/uploaded/i4/1917047079/O1CN01cOgvYi22AEJ7jj9V6_!!2-item_pic.PNG"/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28328" class="proThumb-img " data-index="3:1">
 <img atpanel="3-1,605468103182,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i1/1917047079/O1CN01nuIliq22AEJ5FM7j6_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:28330" class="proThumb-img " data-index="3:2">
 <img atpanel="3-2,605468103182,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/1917047079/O1CN01f3kTAI22AEJ6PtOZ7_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:2954779401" class="proThumb-img " data-index="3:3">
 <img atpanel="3-3,605468103182,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i1/1917047079/O1CN01u63vLS22AEJ9sozvl_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:382328443" class="proThumb-img " data-index="3:4">
 <img atpanel="3-4,605468103182,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i1/1917047079/O1CN01m0T2D222AEJActIYs_!!2-item_pic.png_30x30.jpg"/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">
<a class="tag"><img src="http://tmallfans.cn-hangzhou.oss-pub.aliyun-inc.com/pifu/files/110363/20180912020202.png"/></a>

<em title="10899.00"><b>¥</b>10899.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=605468103182&amp;skuId=4266777221080&amp;standard=1&amp;user_id=2616970884&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Apple/苹果 iPhone 11 Pro Max" data-p="3-11">Apple/苹果 iPhone 11 Pro Max</a>

</div>
<div class="productShop" data-atp="b!3-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2616970884&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
苏宁易购官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1344983838&amp;suid=613234933671e1b9a65e6b9b646fdf9d&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="3-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1.3万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="605468103182" data-nick="苏宁易购官方旗舰店" data-tnick="苏宁易购官方旗舰店" data-display="inline" data-atp="a!3-2,,,,,,,2616970884"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="606306790423" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=606306790423&amp;skuId=4480702130507&amp;standard=1&amp;user_id=2838892713&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="4-10">
<img src="//img.alicdn.com/bao/uploaded/i3/2838892713/O1CN01YaQmE11Vub5mM0L03_!!2838892713.PNG"/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:43832396" class="proThumb-img " data-index="4:1">
 <img atpanel="4-1,606306790423,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1XIORv.Y1gK0jSZFCL6UwqXXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:524272456" class="proThumb-img " data-index="4:2">
 <img atpanel="4-2,606306790423,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB13iOTvYY1gK0jSZTEL6RDQVXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:614390616" class="proThumb-img " data-index="4:3">
 <img atpanel="4-3,606306790423,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1tjyMv1L2gK0jSZPhL6ShvXXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:6503543" class="proThumb-img " data-index="4:4">
 <img atpanel="4-4,606306790423,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1BAOSvYj1gK0jSZFuL6UrHpXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:8988157" class="proThumb-img " data-index="4:5">
 <img atpanel="4-5,606306790423,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1kM1Sv1H2gK0jSZJnL6ST1FXa_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:986234554" class="proThumb-img " data-index="4:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/TB1dmCQvYH1gK0jSZFwL6U7aXXa_30x30.jpg" atpanel="4-6,606306790423,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">

<em title="4999.00"><b>¥</b>4999.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=606306790423&amp;skuId=4480702130507&amp;standard=1&amp;user_id=2838892713&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="HUAWEI HuaWei Mate 30 5G" data-p="4-11">HUAWEI HuaWei Mate 30 5G</a>

</div>
<div class="productShop" data-atp="b!4-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2838892713&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
华为官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1398196606&amp;suid=5af4a045cb7c8fda9d86340047faf827&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="4-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>6.8万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="606306790423" data-nick="华为官方旗舰店" data-tnick="华为官方旗舰店" data-display="inline" data-atp="a!4-2,,,,,,,2838892713"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="598079959720" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=598079959720&amp;skuId=4480708178238&amp;standard=1&amp;user_id=1114511827&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="5-10">
<img src="//img.alicdn.com/bao/uploaded/i3/TB1HF5ebkT2gK0jSZFkcNoIQFXa_015826.jpg"/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="5:1">
 <img atpanel="5-1,598079959720,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/1114511827/O1CN01r4vRMG1PMo9xWPrfQ_!!1114511827.jpg_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:1112056456" class="proThumb-img " data-index="5:2">
 <img atpanel="5-2,598079959720,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i1/1114511827/O1CN01c7q7L01PMo9xWSPen_!!1114511827.jpg_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:1676379702" class="proThumb-img " data-index="5:3">
 <img atpanel="5-3,598079959720,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i1/1114511827/O1CN01knqYEH1PMo9u9eWcp_!!1114511827.jpg_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:441476440" class="proThumb-img " data-index="5:4">
 <img atpanel="5-4,598079959720,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i2/1114511827/O1CN01WsYa1f1PMoAmt3JBe_!!1114511827.png_30x30.jpg"/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1299.00"><b>¥</b>1299.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=598079959720&amp;skuId=4480708178238&amp;standard=1&amp;user_id=1114511827&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="honor/荣耀 荣耀9x" data-p="5-11">honor/荣耀 荣耀9x</a>

</div>
<div class="productShop" data-atp="b!5-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1114511827&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
荣耀官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1260500122&amp;suid=2d6801e9d56f6bbc2c0ee3cd39961adc&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="5-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>14万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="598079959720" data-nick="荣耀官方旗舰店" data-tnick="荣耀官方旗舰店" data-display="inline" data-atp="a!5-2,,,,,,,1114511827"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="600630289146" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=600630289146&amp;skuId=4208790576546&amp;standard=1&amp;user_id=1714128138&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="6-10">
<img src="//img.alicdn.com/bao/uploaded/i7/TB12Ld9eYH1gK0jSZFw6h37aXXa_104124.jpg"/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:381198578" class="proThumb-img " data-index="6:1">
 <img atpanel="6-1,600630289146,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i5/TB1xjB1eWL7gK0jSZFBuSVZZpXa_104052.jpg_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:7855906" class="proThumb-img " data-index="6:2">
 <img atpanel="6-2,600630289146,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i5/TB1VFh5e4D1gK0jSZFs9j6ldVXa_103853.jpg_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:89992009" class="proThumb-img " data-index="6:3">
 <img atpanel="6-3,600630289146,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i4/TB1fvx5e4z1gK0jSZSgAeivwpXa_103743.jpg_30x30.jpg"/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="999.00"><b>¥</b>999.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=600630289146&amp;skuId=4208790576546&amp;standard=1&amp;user_id=1714128138&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="4800万超清四摄 高通骁龙665" data-p="6-11">Xiaomi/小米 Redmi Note 8</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=600630289146&amp;skuId=4208790576546&amp;standard=1&amp;user_id=1714128138&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="4800万超清四摄 高通骁龙665" data-p="6-11">4800万超清四摄 高通骁龙665</a>

</div>
<div class="productShop" data-atp="b!6-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1714128138&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
小米官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1324378865&amp;suid=d05d9e6324a811f4e2cb7918db4c88d3&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="6-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>8.3万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="600630289146" data-nick="小米官方旗舰店" data-tnick="小米官方旗舰店" data-display="inline" data-atp="a!6-2,,,,,,,1714128138"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="587634209193" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=587634209193&amp;skuId=4480191679171&amp;standard=1&amp;user_id=370627083&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="7-10">
<img src="//img.alicdn.com/bao/uploaded/i3/TB1fOtnbDZmx1VjSZFGj3Sx2XXa_025424.jpg"/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:383182043" class="proThumb-img " data-index="7:1">
 <img atpanel="7-1,587634209193,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/TB1VQRNIH2pK1RjSZFsHO1NlXXa_025708.jpg_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:553862854" class="proThumb-img " data-index="7:2">
 <img atpanel="7-2,587634209193,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i2/TB1FXhJIRLoK1RjSZFuNaln0XXa_025702.jpg_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:70535664" class="proThumb-img " data-index="7:3">
 <img atpanel="7-3,587634209193,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i1/370627083/O1CN01FXrxWP22C3sATEURK_!!370627083.jpg_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:88016470" class="proThumb-img " data-index="7:4">
 <img atpanel="7-4,587634209193,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i6/TB1vzdKISzqK1RjSZPxZDw4tVXa_025716.jpg_30x30.jpg"/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="4299.00"><b>¥</b>4299.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=587634209193&amp;skuId=4480191679171&amp;standard=1&amp;user_id=370627083&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="超感观全视屏、超声波屏下指纹" data-p="7-11">Samsung/三星 Galaxy S10 SM-G9730</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=587634209193&amp;skuId=4480191679171&amp;standard=1&amp;user_id=370627083&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="超感观全视屏、超声波屏下指纹" data-p="7-11">超感观全视屏、超声波屏下指纹</a>

</div>
<div class="productShop" data-atp="b!7-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=370627083&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
三星官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1157484706&amp;suid=2ba9c5bf52b349947637a627e5c9a50b&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="7-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1846笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="587634209193" data-nick="三星官方旗舰店" data-tnick="三星官方旗舰店" data-display="inline" data-atp="a!7-2,,,,,,,370627083"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="599251658651" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=599251658651&amp;skuId=4330028301111&amp;standard=1&amp;user_id=883737303&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="8-10">
<img src="//img.alicdn.com/bao/uploaded/i3/TB1o0OCcy_1gK0jSZFq.03paXXa_100855.jpg"/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:119974023" class="proThumb-img " data-index="8:1">
 <img atpanel="8-1,599251658651,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i4/883737303/O1CN01PPzQCE23op11LoBpT_!!883737303.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:1375909291" class="proThumb-img " data-index="8:2">
 <img atpanel="8-2,599251658651,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i2/883737303/O1CN018y49H023op0szGVTN_!!883737303.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:5216309359" class="proThumb-img " data-index="8:3">
 <img atpanel="8-3,599251658651,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/883737303/O1CN0140GpG323op0zokZyB_!!883737303.png_30x30.jpg"/>
 <i/>
 </b>
  <b data-sku="1627207:7554695683" class="proThumb-img " data-index="8:4">
 <img atpanel="8-4,599251658651,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/TB1BEZhzAL0gK0jSZFtL6RQCXXa_30x30.jpg"/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1798.00"><b>¥</b>1798.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=599251658651&amp;skuId=4330028301111&amp;standard=1&amp;user_id=883737303&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="vivo Z5" data-p="8-11">vivo Z5</a>

</div>
<div class="productShop" data-atp="b!8-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=883737303&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
vivo官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1275400539&amp;suid=a5a41320930cc21537b1e9e8773470c3&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="8-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3.0万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="599251658651" data-nick="vivo官方旗舰店" data-tnick="vivo官方旗舰店" data-display="inline" data-atp="a!8-2,,,,,,,883737303"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="594381462179" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=594381462179&amp;skuId=4301474348316&amp;standard=1&amp;user_id=883737303&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="9-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1IcUVeRWD3KVjSZKPqaup7FXa_092737.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:424596754" class="proThumb-img " data-index="9:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB15loReMaH3KVjSZFjHrMFWpXa_093139.jpg_30x30.jpg" atpanel="9-1,594381462179,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:663282071" class="proThumb-img " data-index="9:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1q8AReNiH3KVjSZPf_HJBiVXa_092926.jpg_30x30.jpg" atpanel="9-2,594381462179,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1398.00"><b>¥</b>1398.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=594381462179&amp;skuId=4301474348316&amp;standard=1&amp;user_id=883737303&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="vivo Z5X" data-p="9-11">vivo Z5X</a>

</div>
<div class="productShop" data-atp="b!9-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=883737303&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
vivo官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1221849181&amp;suid=a5a41320930cc21537b1e9e8773470c3&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="9-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>5.1万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="594381462179" data-nick="vivo官方旗舰店" data-tnick="vivo官方旗舰店" data-display="inline" data-atp="a!9-2,,,,,,,883737303"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="602221212439" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=602221212439&amp;skuId=4245293161801&amp;standard=1&amp;user_id=1714128138&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="10-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1714128138/O1CN01YGkMKk29zFkRAnYro_!!1714128138.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28942472" class="proThumb-img " data-index="10:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1714128138/O1CN01kCm0de29zFkRdHo3d_!!1714128138.jpg_30x30.jpg" atpanel="10-1,602221212439,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="699.00"><b>¥</b>699.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=602221212439&amp;skuId=4245293161801&amp;standard=1&amp;user_id=1714128138&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="5000mAh大电量" data-p="10-11">Xiaomi/小米 Redmi 8A</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=602221212439&amp;skuId=4245293161801&amp;standard=1&amp;user_id=1714128138&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="5000mAh大电量" data-p="10-11">5000mAh大电量</a>

</div>
<div class="productShop" data-atp="b!10-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1714128138&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
小米官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1389982286&amp;suid=d05d9e6324a811f4e2cb7918db4c88d3&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="10-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>6.7万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="602221212439" data-nick="小米官方旗舰店" data-tnick="小米官方旗舰店" data-display="inline" data-atp="a!10-2,,,,,,,1714128138"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="594834276618" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=594834276618&amp;skuId=4487745314467&amp;standard=1&amp;user_id=1114511827&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="11-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/TB18jSxXL5G3KVjSZPxeCbI3XXa_121812.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1634544694" class="proThumb-img " data-index="11:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1114511827/O1CN01wS3Zdi1PMo9owocSB_!!1114511827.jpg_30x30.jpg" atpanel="11-1,594834276618,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:204788182" class="proThumb-img " data-index="11:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1114511827/O1CN01Kd0RXD1PMo8qVVc43_!!1114511827.jpg_30x30.jpg" atpanel="11-2,594834276618,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4393000428" class="proThumb-img " data-index="11:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1114511827/O1CN01TarXhM1PMo8rnifQC_!!1114511827.jpg_30x30.jpg" atpanel="11-3,594834276618,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2299.00"><b>¥</b>2299.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=594834276618&amp;skuId=4487745314467&amp;standard=1&amp;user_id=1114511827&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="honor/荣耀 荣耀20 pro" data-p="11-11">honor/荣耀 荣耀20 pro</a>

</div>
<div class="productShop" data-atp="b!11-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1114511827&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
荣耀官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1224854975&amp;suid=2d6801e9d56f6bbc2c0ee3cd39961adc&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="11-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3.4万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="594834276618" data-nick="荣耀官方旗舰店" data-tnick="荣耀官方旗舰店" data-display="inline" data-atp="a!11-2,,,,,,,1114511827"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="603070922282" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=603070922282&amp;skuId=4420793127771&amp;standard=1&amp;user_id=901409638&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="12-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1taKvhuL2gK0jSZFm1177iXXa_121513.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:5710297862" class="proThumb-img " data-index="12:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1kXxqjYj1gK0jSZFuJGkrHpXa_112424.jpg_30x30.jpg" atpanel="12-1,603070922282,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1899.00"><b>¥</b>1899.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=603070922282&amp;skuId=4420793127771&amp;standard=1&amp;user_id=901409638&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="OPPO K5" data-p="12-11">OPPO K5</a>

</div>
<div class="productShop" data-atp="b!12-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=901409638&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
OPPO官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1350878395&amp;suid=0d961e929500cf93747de4779ba7a9fb&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="12-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3.0万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="603070922282" data-nick="oppo官方旗舰店" data-tnick="oppo官方旗舰店" data-display="inline" data-atp="a!12-2,,,,,,,901409638"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="587770474543" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=587770474543&amp;skuId=4313218293375&amp;standard=1&amp;user_id=370627083&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="13-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB14oJ3INjaK1RjSZFAjfvdLFXa_030957.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:383182043" class="proThumb-img " data-index="13:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1w68YIMHqK1RjSZJnQUvNLpXa_031303.jpg_30x30.jpg" atpanel="13-1,587770474543,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:553862854" class="proThumb-img " data-index="13:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB19m8UIQvoK1RjSZFNZ6AxMVXa_031258.jpg_30x30.jpg" atpanel="13-2,587770474543,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:70535664" class="proThumb-img " data-index="13:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/370627083/O1CN01ZJyVTB22C3s6ob9Qy_!!370627083.jpg_30x30.jpg" atpanel="13-3,587770474543,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:88016470" class="proThumb-img " data-index="13:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1teJKIPDpK1RjSZFrrUW78VXa_031307.jpg_30x30.jpg" atpanel="13-4,587770474543,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="5099.00"><b>¥</b>5099.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=587770474543&amp;skuId=4313218293375&amp;standard=1&amp;user_id=370627083&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="超感观全视屏、超声波屏下指纹" data-p="13-11">Samsung/三星 Galaxy S10+ SM-G9750</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=587770474543&amp;skuId=4313218293375&amp;standard=1&amp;user_id=370627083&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="超感观全视屏、超声波屏下指纹" data-p="13-11">超感观全视屏、超声波屏下指纹</a>

</div>
<div class="productShop" data-atp="b!13-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=370627083&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
三星官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1157510661&amp;suid=2ba9c5bf52b349947637a627e5c9a50b&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="13-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1264笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="587770474543" data-nick="三星官方旗舰店" data-tnick="三星官方旗舰店" data-display="inline" data-atp="a!13-2,,,,,,,370627083"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="602613660417" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=602613660417&amp;skuId=4405281055077&amp;standard=1&amp;user_id=901409638&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="14-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1xWL5jrr1gK0jSZR09U2P8XXa_011932.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:117397905" class="proThumb-img " data-index="14:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1PqQFhET1gK0jSZFh5UKAtVXa_112714.jpg_30x30.jpg" atpanel="14-1,602613660417,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:1366063813" class="proThumb-img " data-index="14:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB17YQGhrr1gK0jSZR04cYP8XXa_112943.jpg_30x30.jpg" atpanel="14-2,602613660417,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="3199.00"><b>¥</b>3199.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=602613660417&amp;skuId=4405281055077&amp;standard=1&amp;user_id=901409638&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="OPPO Reno Ace" data-p="14-11">OPPO Reno Ace</a>

</div>
<div class="productShop" data-atp="b!14-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=901409638&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
OPPO官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1350842340&amp;suid=0d961e929500cf93747de4779ba7a9fb&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="14-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>9894笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="602613660417" data-nick="oppo官方旗舰店" data-tnick="oppo官方旗舰店" data-display="inline" data-atp="a!14-2,,,,,,,901409638"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="605943470549" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=605943470549&amp;skuId=4320470601348&amp;standard=1&amp;user_id=2088045547&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="15-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/2838892713/O1CN01T0MM8R1Vub5izN1VL_!!2838892713.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="15:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/2838892713/O1CN01T0MM8R1Vub5izN1VL_!!2838892713.jpg_30x30.jpg" atpanel="15-1,605943470549,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:11103014" class="proThumb-img " data-index="15:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/2838892713/O1CN01EufC2d1Vub5kV9bqJ_!!2838892713.jpg_30x30.jpg" atpanel="15-2,605943470549,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:141692791" class="proThumb-img " data-index="15:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2838892713/O1CN01vgS8o41Vub5gsvvbs_!!2838892713.jpg_30x30.jpg" atpanel="15-3,605943470549,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2787108685" class="proThumb-img " data-index="15:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/3937219703/O1CN01QERbu72LY1c8ClX7V_!!3937219703.jpg_30x30.jpg" atpanel="15-4,605943470549,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2799335837" class="proThumb-img " data-index="15:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/3937219703/O1CN01bfbern2LY1cBJRFN3_!!3937219703.jpg_30x30.jpg" atpanel="15-5,605943470549,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:297498935" class="proThumb-img " data-index="15:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i4/2838892713/O1CN01eSiMI41Vub5izMQ13_!!2838892713.jpg_30x30.jpg" atpanel="15-6,605943470549,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
  <b data-sku="1627207:3006404641" class="proThumb-img " data-index="15:7">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i2/3937219703/O1CN01PFCRUA2LY1bzwOKEL_!!3937219703.jpg_30x30.jpg" atpanel="15-7,605943470549,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">

<em title="899.00"><b>¥</b>899.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=605943470549&amp;skuId=4320470601348&amp;standard=1&amp;user_id=2088045547&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="HUAWEI 华为畅享10" data-p="15-11">HUAWEI 华为畅享10</a>

</div>
<div class="productShop" data-atp="b!15-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2088045547&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
京合旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1390542230&amp;suid=a24cf05bc74d97f47b873c561adee3e0&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="15-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>5.5万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="605943470549" data-nick="京合旗舰店" data-tnick="京合旗舰店" data-display="inline" data-atp="a!15-2,,,,,,,2088045547"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="577950907330" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=577950907330&amp;skuId=4300174594864&amp;standard=1&amp;user_id=268451883&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="16-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1syulv.Y1gK0jSZFM9cqWcVXa_084501.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28328" class="proThumb-img " data-index="16:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1wumWDNTpK1RjSZFMfUnG_VXa_043627.jpg_30x30.jpg" atpanel="16-1,577950907330,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28330" class="proThumb-img " data-index="16:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1zyWTDOrpK1RjSZFhfUlSdXXa_043627.jpg_30x30.jpg" atpanel="16-2,577950907330,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="6888.00"><b>¥</b>6888.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=577950907330&amp;skuId=4300174594864&amp;standard=1&amp;user_id=268451883&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="配备A12仿生芯片，支持双卡" data-p="16-11">Apple/苹果 iPhone XS Max</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=577950907330&amp;skuId=4300174594864&amp;standard=1&amp;user_id=268451883&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="配备A12仿生芯片，支持双卡" data-p="16-11">配备A12仿生芯片，支持双卡</a>

</div>
<div class="productShop" data-atp="b!16-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=268451883&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
三际数码官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1057098687&amp;suid=5a7db1626844d95e0aea057e0f123a4d&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="16-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3744笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="577950907330" data-nick="三际数码官方旗舰店" data-tnick="三际数码官方旗舰店" data-display="inline" data-atp="a!16-2,,,,,,,268451883"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="577456372778" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=577456372778&amp;skuId=4380370911164&amp;standard=1&amp;user_id=1776456424&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="17-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB17BOgvWL7gK0jSZFB_UdZZpXa_083942.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28328" class="proThumb-img " data-index="17:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB1e207X9zqK1RjSZPxk2Z4tVXa_025101.jpg_30x30.jpg" atpanel="17-1,577456372778,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28330" class="proThumb-img " data-index="17:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1jf07X9zqK1RjSZPxk2Z4tVXa_025101.jpg_30x30.jpg" atpanel="17-2,577456372778,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:382328443" class="proThumb-img " data-index="17:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1fbl9X4TpK1RjSZR0k2YEwXXa_025101.jpg_30x30.jpg" atpanel="17-3,577456372778,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="5398.00"><b>¥</b>5398.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=577456372778&amp;skuId=4380370911164&amp;standard=1&amp;user_id=1776456424&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Apple/苹果 iPhone XS" data-p="17-11">Apple/苹果 iPhone XS</a>

</div>
<div class="productShop" data-atp="b!17-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1776456424&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
中国移动官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1058639181&amp;suid=eb1dd33ca961240c80daf99e70459da7&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="17-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>376笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="577456372778" data-nick="中国移动官方旗舰店" data-tnick="中国移动官方旗舰店" data-display="inline" data-atp="a!17-2,,,,,,,1776456424"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="596753542423" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=596753542423&amp;skuId=4498925723829&amp;standard=1&amp;user_id=2088045547&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="18-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2838892713/O1CN01nRiF3J1Vub400szbr_!!2838892713.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1278264011" class="proThumb-img " data-index="18:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/2838892713/O1CN01iRJ1Yx1Vub3xfxqCS_!!2838892713.jpg_30x30.jpg" atpanel="18-1,596753542423,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:43832396" class="proThumb-img " data-index="18:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/2838892713/O1CN01iv6azS1Vub3xziReN_!!2838892713.jpg_30x30.jpg" atpanel="18-2,596753542423,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4555732106" class="proThumb-img " data-index="18:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2838892713/O1CN01DaJUoS1Vub3xg07Vb_!!2838892713.jpg_30x30.jpg" atpanel="18-3,596753542423,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5775374039" class="proThumb-img " data-index="18:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN019AdgeD2LY1cJgrb9h_!!3937219703.jpg_30x30.jpg" atpanel="18-4,596753542423,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5818487898" class="proThumb-img " data-index="18:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN0196SHGg2LY1cKvqf7v_!!3937219703.jpg_30x30.jpg" atpanel="18-5,596753542423,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2599.00"><b>¥</b>2599.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=596753542423&amp;skuId=4498925723829&amp;standard=1&amp;user_id=2088045547&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="HUAWEI nova 5 Pro" data-p="18-11">HUAWEI nova 5 Pro</a>

</div>
<div class="productShop" data-atp="b!18-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2088045547&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
京合旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1247033188&amp;suid=a24cf05bc74d97f47b873c561adee3e0&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="18-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>5.7万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="596753542423" data-nick="京合旗舰店" data-tnick="京合旗舰店" data-display="inline" data-atp="a!18-2,,,,,,,2088045547"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="580273092631" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=580273092631&amp;skuId=4323450429853&amp;standard=1&amp;user_id=1776456424&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="19-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1917047079/O1CN0122AEDTONiTEEAnd_!!1917047079.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28320" class="proThumb-img " data-index="19:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1917047079/O1CN0122AEDV7xLbR8wMv_!!1917047079.jpg_30x30.jpg" atpanel="19-1,580273092631,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28324" class="proThumb-img " data-index="19:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1917047079/O1CN0122AEDSCUeVQxUWQ_!!1917047079.jpg_30x30.jpg" atpanel="19-2,580273092631,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28326" class="proThumb-img " data-index="19:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1917047079/O1CN0122AEDNRubJERqkK_!!1917047079.jpg_30x30.jpg" atpanel="19-3,580273092631,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28341" class="proThumb-img " data-index="19:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1917047079/O1CN0122AEDSCWC4C6KUi_!!1917047079.jpg_30x30.jpg" atpanel="19-4,580273092631,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="4598.00"><b>¥</b>4598.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=580273092631&amp;skuId=4323450429853&amp;standard=1&amp;user_id=1776456424&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Apple/苹果 iPhone XR" data-p="19-11">Apple/苹果 iPhone XR</a>

</div>
<div class="productShop" data-atp="b!19-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1776456424&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
中国移动官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1089679943&amp;suid=eb1dd33ca961240c80daf99e70459da7&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="19-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1.2万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="580273092631" data-nick="中国移动官方旗舰店" data-tnick="中国移动官方旗舰店" data-display="inline" data-atp="a!19-2,,,,,,,1776456424"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="606209656084" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=606209656084&amp;skuId=4424188959782&amp;standard=1&amp;user_id=2201438992231&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="20-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1714128138/O1CN01AwMqe229zFk7QWcDQ_!!1714128138.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:34749180" class="proThumb-img " data-index="20:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1714128138/O1CN01A4Zfd629zFk8AaeoC_!!1714128138.jpg_30x30.jpg" atpanel="20-1,606209656084,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4404456" class="proThumb-img " data-index="20:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1714128138/O1CN01jQl52F29zFkArzBRN_!!1714128138.jpg_30x30.jpg" atpanel="20-2,606209656084,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4841571" class="proThumb-img " data-index="20:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1714128138/O1CN01mtbEAm29zFk875gF4_!!1714128138.jpg_30x30.jpg" atpanel="20-3,606209656084,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5732045757" class="proThumb-img " data-index="20:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1tEX_gET1gK0jSZFhd0CAtVXa_095524.jpg_30x30.jpg" atpanel="20-4,606209656084,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:66521134" class="proThumb-img " data-index="20:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1714128138/O1CN01KwgvcE29zFk0Klv0m_!!1714128138.jpg_30x30.jpg" atpanel="20-5,606209656084,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="3029.00"><b>¥</b>3029.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=606209656084&amp;skuId=4424188959782&amp;standard=1&amp;user_id=2201438992231&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="骁龙855Plus处理器 大容量大内存" data-p="20-11">Xiaomi/小米 Redmi K20 Pro 尊享版</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=606209656084&amp;skuId=4424188959782&amp;standard=1&amp;user_id=2201438992231&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="骁龙855Plus处理器 大容量大内存" data-p="20-11">骁龙855Plus处理器 大容量大内存</a>

</div>
<div class="productShop" data-atp="b!20-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2201438992231&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
信息港数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1352962961&amp;suid=e2cb98b1dbdafb043c25ea0494ce47e1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="20-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>646笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="606209656084" data-nick="信息港数码专营店" data-tnick="信息港数码专营店" data-display="inline" data-atp="a!20-2,,,,,,,2201438992231"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="583757936542" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=583757936542&amp;skuId=3939268509009&amp;standard=1&amp;user_id=1963544026&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="21-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1ue5OPIfpK1RjSZFOS3a6nFXa_052136.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="21:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1v9_XbAP2gK0jSZPxvq9cQpXa_112348.jpg_30x30.jpg" atpanel="21-1,583757936542,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:14324282" class="proThumb-img " data-index="21:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1PZHbbBr0gK0jSZFnmAYRRXXa_112234.jpg_30x30.jpg" atpanel="21-2,583757936542,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:297498935" class="proThumb-img " data-index="21:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1_TPabAL0gK0jSZFA81MA9pXa_112258.jpg_30x30.jpg" atpanel="21-3,583757936542,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:3515105317" class="proThumb-img " data-index="21:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/3937219703/O1CN01TR6K8h2LY1c8hLbVa_!!3937219703.jpg_30x30.jpg" atpanel="21-4,583757936542,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:3820872766" class="proThumb-img " data-index="21:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/3937219703/O1CN016fHRYD2LY1cBkyCRw_!!3937219703.jpg_30x30.jpg" atpanel="21-5,583757936542,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:48897196" class="proThumb-img " data-index="21:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i5/TB18Wa9bqL7gK0jSZFBvcJZZpXa_112316.jpg_30x30.jpg" atpanel="21-6,583757936542,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
  <b data-sku="1627207:5460221331" class="proThumb-img " data-index="21:7">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN01YqbEOw2LY1c6ubpQz_!!3937219703.jpg_30x30.jpg" atpanel="21-7,583757936542,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">

<em title="849.00"><b>¥</b>849.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=583757936542&amp;skuId=3939268509009&amp;standard=1&amp;user_id=1963544026&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="6.26英寸珍珠屏 AI长续航" data-p="21-11">HUAWEI 畅享9</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=583757936542&amp;skuId=3939268509009&amp;standard=1&amp;user_id=1963544026&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="6.26英寸珍珠屏 AI长续航" data-p="21-11">6.26英寸珍珠屏 AI长续航</a>

</div>
<div class="productShop" data-atp="b!21-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1963544026&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
博海宇通数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1121267822&amp;suid=8ce2d34f5ffd172b8978b33a8398be30&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="21-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1.1万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="583757936542" data-nick="博海宇通数码专营店" data-tnick="博海宇通数码专营店" data-display="inline" data-atp="a!21-2,,,,,,,1963544026"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="608151421319" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=608151421319&amp;skuId=4445982995478&amp;standard=1&amp;user_id=1902393607&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="22-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2206774295362/O1CN01ClbB1u1pTqH8ZzyPs_!!2206774295362-0-scmitem40000.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28320" class="proThumb-img " data-index="22:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3402329517/O1CN01esKDmh2KApvYvk7LF_!!3402329517.jpg_30x30.jpg" atpanel="22-1,608151421319,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28324" class="proThumb-img " data-index="22:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3402329517/O1CN01MXbHA92KApvgV7Y8G_!!3402329517.jpg_30x30.jpg" atpanel="22-2,608151421319,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28326" class="proThumb-img " data-index="22:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3402329517/O1CN01RpXm4N2KApvda47pj_!!3402329517.jpg_30x30.jpg" atpanel="22-3,608151421319,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28329" class="proThumb-img " data-index="22:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3402329517/O1CN01n9gOCX2KApveovbLR_!!3402329517.jpg_30x30.jpg" atpanel="22-4,608151421319,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28335" class="proThumb-img " data-index="22:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3402329517/O1CN01cbVt3j2KApvdaCFUC_!!3402329517.jpg_30x30.jpg" atpanel="22-5,608151421319,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28341" class="proThumb-img " data-index="22:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i4/3402329517/O1CN019Zcy1g2KApvhiJJAj_!!3402329517.jpg_30x30.jpg" atpanel="22-6,608151421319,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">

<em title="5757.42"><b>¥</b>5757.42</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=608151421319&amp;skuId=4445982995478&amp;standard=1&amp;user_id=1902393607&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Apple/苹果 Apple iPhone 11" data-p="22-11">Apple/苹果 Apple iPhone 11</a>

</div>
<div class="productShop" data-atp="b!22-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1902393607&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
四川移动官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1440334676&amp;suid=97d1f3b1a488ac899e26f8435f12e40d&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="22-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>2461笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="608151421319" data-nick="四川移动官方旗舰店" data-tnick="四川移动官方旗舰店" data-display="inline" data-atp="a!22-2,,,,,,,1902393607"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="607390476199" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=607390476199&amp;skuId=4318020536540&amp;standard=1&amp;user_id=2201415337596&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="23-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1xHH3HHvpK1RjSZFqmR.XUVXa_123431.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:107121" class="proThumb-img " data-index="23:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1714128138/O1CN01JqDpat29zFguplHHs_!!1714128138.jpg_30x30.jpg" atpanel="23-1,607390476199,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2904182500" class="proThumb-img " data-index="23:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1714128138/O1CN01VQp4Th29zFjcOfPJL_!!1714128138.png_30x30.jpg" atpanel="23-2,607390476199,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2904182501" class="proThumb-img " data-index="23:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1714128138/O1CN01cM3dOv29zFjZknWSr_!!1714128138.png_30x30.jpg" atpanel="23-3,607390476199,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:386658051" class="proThumb-img " data-index="23:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1714128138/O1CN01ndyzDv29zFjb25veL_!!1714128138.png_30x30.jpg" atpanel="23-4,607390476199,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7400339710" class="proThumb-img " data-index="23:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/3937219703/O1CN01cDbUOh2LY1c1UAdCn_!!3937219703.jpg_30x30.jpg" atpanel="23-5,607390476199,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2198.00"><b>¥</b>2198.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=607390476199&amp;skuId=4318020536540&amp;standard=1&amp;user_id=2201415337596&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Xiaomi/小米 小米9" data-p="23-11">Xiaomi/小米 小米9</a>

</div>
<div class="productShop" data-atp="b!23-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2201415337596&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
连盛数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1152764912&amp;suid=151211822341c646b02d4f0804639a7a&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="23-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>602笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="607390476199" data-nick="连盛数码专营店" data-tnick="连盛数码专营店" data-display="inline" data-atp="a!23-2,,,,,,,2201415337596"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="602618770018" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=602618770018&amp;skuId=4221197508350&amp;standard=1&amp;user_id=697028616&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="24-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB13SaTl7T2gK0jSZFkybcIQFXa_023836.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:5684966747" class="proThumb-img " data-index="24:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB14FeLykY2gK0jSZFgNgQ5OFXa_095343.jpg_30x30.jpg" atpanel="24-1,602618770018,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5684994409" class="proThumb-img " data-index="24:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1kzyLybr1gK0jSZR0iFPP8XXa_101945.jpg_30x30.jpg" atpanel="24-2,602618770018,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="4998.00"><b>¥</b>4998.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=602618770018&amp;skuId=4221197508350&amp;standard=1&amp;user_id=697028616&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="即将上市 加购抽NEX 3手机" data-p="24-11">vivo NEX 3 5G</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=602618770018&amp;skuId=4221197508350&amp;standard=1&amp;user_id=697028616&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="即将上市 加购抽NEX 3手机" data-p="24-11">即将上市 加购抽NEX 3手机</a>

</div>
<div class="productShop" data-atp="b!24-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=697028616&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
vivo天诚专卖店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1331085392&amp;suid=41d3d0d74be137dbdde073eb6d5e8b4b&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="24-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>436笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="602618770018" data-nick="vivo天诚专卖店" data-tnick="vivo天诚专卖店" data-display="inline" data-atp="a!24-2,,,,,,,697028616"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="576304458649" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=576304458649&amp;skuId=4327212026523&amp;standard=1&amp;user_id=268451883&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="25-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1SuqasbH1gK0jSZFwhqU7aXXa_030637.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="25:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1bZ6SNFzqK1RjSZFoUzDfcXXa_040959.jpg_30x30.jpg" atpanel="25-1,576304458649,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:110291612" class="proThumb-img " data-index="25:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1Ea_MNSzqK1RjSZFL61.n2XXa_041338.jpg_30x30.jpg" atpanel="25-2,576304458649,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:1112056456" class="proThumb-img " data-index="25:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1A3LRNQvoK1RjSZFD5TdY3pXa_041115.jpg_30x30.jpg" atpanel="25-3,576304458649,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:1676379702" class="proThumb-img " data-index="25:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1Fm22NIfpK1RjSZFO58C6nFXa_040850.jpg_30x30.jpg" atpanel="25-4,576304458649,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1349.00"><b>¥</b>1349.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=576304458649&amp;skuId=4327212026523&amp;standard=1&amp;user_id=268451883&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="honor/荣耀 荣耀8X" data-p="25-11">honor/荣耀 荣耀8X</a>

</div>
<div class="productShop" data-atp="b!25-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=268451883&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
三际数码官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1038927824&amp;suid=5a7db1626844d95e0aea057e0f123a4d&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="25-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3185笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="576304458649" data-nick="三际数码官方旗舰店" data-tnick="三际数码官方旗舰店" data-display="inline" data-atp="a!25-2,,,,,,,268451883"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="606672237166" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=606672237166&amp;skuId=4430559022783&amp;standard=1&amp;user_id=2201435294972&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="26-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB18pmBlKL2gK0jSZFmtu77iXXa_103526.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:2293241167" class="proThumb-img " data-index="26:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1714128138/O1CN01CmPcxs29zFkhwwcAG_!!1714128138.png_30x30.jpg" atpanel="26-1,606672237166,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:6285699180" class="proThumb-img " data-index="26:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1714128138/O1CN01WdgEKN29zFkl5p1Ca_!!1714128138.png_30x30.jpg" atpanel="26-2,606672237166,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:6286023544" class="proThumb-img " data-index="26:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1714128138/O1CN01CmPcxs29zFkhwwcAG_!!1714128138.png_30x30.jpg" atpanel="26-3,606672237166,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2588.00"><b>¥</b>2588.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=606672237166&amp;skuId=4430559022783&amp;standard=1&amp;user_id=2201435294972&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Xiaomi/小米 小米CC9 PRO" data-p="26-11">Xiaomi/小米 小米CC9 PRO</a>

</div>
<div class="productShop" data-atp="b!26-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2201435294972&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
迈微数码旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1415870011&amp;suid=55521e6ef979bc79979176d01fc37cf3&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="26-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>7970笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="606672237166" data-nick="迈微数码旗舰店" data-tnick="迈微数码旗舰店" data-display="inline" data-atp="a!26-2,,,,,,,2201435294972"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="576793268677" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=576793268677&amp;skuId=4264728457664&amp;standard=1&amp;user_id=210910611&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="27-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1bOPIH3DqK1RjSZSyx9CxEVXa_052910.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="27:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB17kq0tHZnBKNjSZFGkUzt3FXa_042707.jpg_30x30.jpg" atpanel="27-1,576793268677,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:1112056456" class="proThumb-img " data-index="27:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1owvstAZmBKNjSZPikUxFNVXa_042707.jpg_30x30.jpg" atpanel="27-2,576793268677,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7393246800" class="proThumb-img " data-index="27:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01foWeXr2LY1c9NxgZZ_!!3937219703.jpg_30x30.jpg" atpanel="27-3,576793268677,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7393264699" class="proThumb-img " data-index="27:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN015jKrmp2LY1c9KmVdj_!!3937219703.jpg_30x30.jpg" atpanel="27-4,576793268677,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7393322310" class="proThumb-img " data-index="27:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01WqEQyH2LY1cB6zSnj_!!3937219703.jpg_30x30.jpg" atpanel="27-5,576793268677,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1199.00"><b>¥</b>1199.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=576793268677&amp;skuId=4264728457664&amp;standard=1&amp;user_id=210910611&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="honor/荣耀 荣耀8X MAX" data-p="27-11">honor/荣耀 荣耀8X MAX</a>

</div>
<div class="productShop" data-atp="b!27-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=210910611&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
晋商数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1042332469&amp;suid=416ab1b300dae4bb4ec59f47a3ee0cd6&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="27-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1728笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="576793268677" data-nick="晋商数码专营店" data-tnick="晋商数码专营店" data-display="inline" data-atp="a!27-2,,,,,,,210910611"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="605477484596" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=605477484596&amp;skuId=4246808537686&amp;standard=1&amp;user_id=2432146763&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="28-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3016151463/O1CN014r2ZkV1Mg60aVG7mw_!!3016151463.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1364483721" class="proThumb-img " data-index="28:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2432146763/O1CN01p5rPcz1zpV9taAykz_!!2432146763.jpg_30x30.jpg" atpanel="28-1,605477484596,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:299872681" class="proThumb-img " data-index="28:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/2432146763/O1CN01mm6hDY1zpV9ogHTGH_!!2432146763.jpg_30x30.jpg" atpanel="28-2,605477484596,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="3199.00"><b>¥</b>3199.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=605477484596&amp;skuId=4246808537686&amp;standard=1&amp;user_id=2432146763&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="OnePlus/一加 HD1900" data-p="28-11">OnePlus/一加 HD1900</a>

</div>
<div class="productShop" data-atp="b!28-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2432146763&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
一加创华威专卖店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1389935839&amp;suid=ed2238a85ddf3888fca2130d4eb9723f&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="28-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3419笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="605477484596" data-nick="一加创华威专卖店" data-tnick="一加创华威专卖店" data-display="inline" data-atp="a!28-2,,,,,,,2432146763"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="588744988537" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=588744988537&amp;skuId=4034648040125&amp;standard=1&amp;user_id=2215302589&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="29-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1UCd7KNnaK1RjSZFBOHQW7VXa_050737.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="29:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB1SoScbbY1gK0jSZTEHRJDQVXa_013732.jpg_30x30.jpg" atpanel="29-1,588744988537,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:3285332" class="proThumb-img " data-index="29:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1rTEEK3HqK1RjSZFgP3W7JXXa_063242.jpg_30x30.jpg" atpanel="29-2,588744988537,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:830264818" class="proThumb-img " data-index="29:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1RK9cboY1gK0jSZFClbwwqXXa_013701.jpg_30x30.jpg" atpanel="29-3,588744988537,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1799.00"><b>¥</b>1799.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=588744988537&amp;skuId=4034648040125&amp;standard=1&amp;user_id=2215302589&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="3200万立体美颜，让本色更出色" data-p="29-11">HUAWEI nova 4e</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=588744988537&amp;skuId=4034648040125&amp;standard=1&amp;user_id=2215302589&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="3200万立体美颜，让本色更出色" data-p="29-11">3200万立体美颜，让本色更出色</a>

</div>
<div class="productShop" data-atp="b!29-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2215302589&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
蓝港数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1166447296&amp;suid=35a4c8edc76508dc40c3400c4d505c4d&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="29-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>6642笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="588744988537" data-nick="蓝港数码专营店" data-tnick="蓝港数码专营店" data-display="inline" data-atp="a!29-2,,,,,,,2215302589"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="589418068757" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=589418068757&amp;skuId=4235193641485&amp;user_id=2986639056&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="30-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1SJc8hpT7gK0jSZFp4P1TkpXa_034632.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28942472" class="proThumb-img " data-index="30:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/2986639056/O1CN01Yir9j42GlhJemJbwU_!!2986639056.jpg_30x30.jpg" atpanel="30-1,589418068757,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="9998.00"><b>¥</b>9998.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=589418068757&amp;skuId=4235193641485&amp;user_id=2986639056&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="首款消费者级别可折叠柔性屏手机" data-p="30-11">柔宇 柔派折叠屏<span class="H">手机</span></a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=589418068757&amp;skuId=4235193641485&amp;user_id=2986639056&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="首款消费者级别可折叠柔性屏手机" data-p="30-11">首款消费者级别可折叠柔性屏手机</a>

</div>
<div class="productShop" data-atp="b!30-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2986639056&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
柔宇数码旗舰店
</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>118笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="589418068757" data-nick="柔宇数码旗舰店" data-tnick="柔宇数码旗舰店" data-display="inline" data-atp="a!30-2,,,,,,,2986639056"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="597343975159" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=597343975159&amp;skuId=4324592971297&amp;standard=1&amp;user_id=1730436394&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="31-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB14kUhhiLaK1RjSZFxlECmPFXa_100611.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="31:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1sPLPhbvpK1RjSZPipAfmwXXa_094239.jpg_30x30.jpg" atpanel="31-1,597343975159,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2880283756" class="proThumb-img " data-index="31:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1710936647/O1CN01ADAkZC1yyN9EC0f9G_!!1710936647.jpg_30x30.jpg" atpanel="31-2,597343975159,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2909000275" class="proThumb-img " data-index="31:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1710936647/O1CN01EA5RDg1yyN9DmoFkO_!!1710936647.jpg_30x30.jpg" atpanel="31-3,597343975159,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2909000277" class="proThumb-img " data-index="31:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1710936647/O1CN01asVv6J1yyN9FTcTzn_!!1710936647.jpg_30x30.jpg" atpanel="31-4,597343975159,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4513375" class="proThumb-img " data-index="31:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1Lm2ThcfpK1RjSZFOGoK6nFXa_094250.jpg_30x30.jpg" atpanel="31-5,597343975159,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4733570511" class="proThumb-img " data-index="31:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i4/268451883/O1CN01aoCn6j1PmSKYFzC5G_!!268451883.jpg_30x30.jpg" atpanel="31-6,597343975159,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
  <b data-sku="1627207:48897196" class="proThumb-img " data-index="31:7">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i8/TB1TcrOhhTpK1RjSZFG3O3HqFXa_094311.jpg_30x30.jpg" atpanel="31-7,597343975159,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">

<em title="849.00"><b>¥</b>849.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=597343975159&amp;skuId=4324592971297&amp;standard=1&amp;user_id=1730436394&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="6.5英寸全面屏 1600万四摄" data-p="31-11">HUAWEI 畅享9 PLUS</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=597343975159&amp;skuId=4324592971297&amp;standard=1&amp;user_id=1730436394&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="6.5英寸全面屏 1600万四摄" data-p="31-11">6.5英寸全面屏 1600万四摄</a>

</div>
<div class="productShop" data-atp="b!31-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1730436394&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
和来达数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1086203236&amp;suid=dc8486e32db242b7f7fd4a6551eabb43&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="31-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1.8万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="597343975159" data-nick="和来达数码专营店" data-tnick="和来达数码专营店" data-display="inline" data-atp="a!31-2,,,,,,,1730436394"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="596126230623" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=596126230623&amp;skuId=4141846385658&amp;standard=1&amp;user_id=1659902905&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="32-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB1kRxtrUT1gK0jSZFrIpZNCXXa_022331.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="32:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB1jA..RyLaK1RjSZFxAFymPFXa_032241.jpg_30x30.jpg" atpanel="32-1,596126230623,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:33580367" class="proThumb-img " data-index="32:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB12DgHRCzqK1RjSZFLN2gn2XXa_032123.jpg_30x30.jpg" atpanel="32-2,596126230623,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:72875631" class="proThumb-img " data-index="32:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1ej.lknZmx1VjSZFGsf9x2XXa_032218.jpg_30x30.jpg" atpanel="32-3,596126230623,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="858.00"><b>¥</b>858.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=596126230623&amp;skuId=4141846385658&amp;standard=1&amp;user_id=1659902905&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="honor/荣耀 荣耀10青春版" data-p="32-11">honor/荣耀 荣耀10青春版</a>

</div>
<div class="productShop" data-atp="b!32-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1659902905&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
久汇数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1108016017&amp;suid=7acea65a3902223db000aed1128680cd&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="32-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1.2万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="596126230623" data-nick="久汇数码专营店" data-tnick="久汇数码专营店" data-display="inline" data-atp="a!32-2,,,,,,,1659902905"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="609317899740" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=609317899740&amp;skuId=4461336355528&amp;standard=1&amp;user_id=2074230553&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="33-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1X86bqLb2gK0jSZK94GiEgFXa_055048.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:157741875" class="proThumb-img " data-index="33:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1spsLp1bviK0jSZFNH7WApXXa_061141.jpg_30x30.jpg" atpanel="33-1,609317899740,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:16118371" class="proThumb-img " data-index="33:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1t3bfqUH1gK0jSZSywTNtlpXa_061124.jpg_30x30.jpg" atpanel="33-2,609317899740,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:189116877" class="proThumb-img " data-index="33:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1fmLkqHj1gK0jSZFuTh7rHpXa_061155.jpg_30x30.jpg" atpanel="33-3,609317899740,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="3298.00"><b>¥</b>3298.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=609317899740&amp;skuId=4461336355528&amp;standard=1&amp;user_id=2074230553&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="vivo X30" data-p="33-11">vivo X30</a>

</div>
<div class="productShop" data-atp="b!33-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2074230553&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
vivo衡视专卖店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1454394518&amp;suid=a32e7718a6add4f9901ad4d8a073ad02&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="33-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1.3万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="609317899740" data-nick="vivo衡视专卖店" data-tnick="vivo衡视专卖店" data-display="inline" data-atp="a!33-2,,,,,,,2074230553"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="602774989212" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=602774989212&amp;skuId=4248406504946&amp;standard=1&amp;user_id=2200766936524&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="34-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1.hxWgUT1gK0jSZFhgVeAtVXa_025912.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:111327" class="proThumb-img " data-index="34:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/TB1pL0sykL0gK0jSZFtL6RQCXXa_30x30.jpg" atpanel="34-1,602774989212,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:1703736835" class="proThumb-img " data-index="34:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2200766936524/O1CN019MurwA1y42Udwx9zo_!!2200766936524.jpg_30x30.jpg" atpanel="34-2,602774989212,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:824368734" class="proThumb-img " data-index="34:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2200766936524/O1CN01sfMcEc1y42UbiWoHF_!!2200766936524.jpg_30x30.jpg" atpanel="34-3,602774989212,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1599.00"><b>¥</b>1599.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=602774989212&amp;skuId=4248406504946&amp;standard=1&amp;user_id=2200766936524&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="realme X2" data-p="34-11">realme X2</a>

</div>
<div class="productShop" data-atp="b!34-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2200766936524&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
realme官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1347501219&amp;suid=d6d3363919b11e43d6600014627b7da5&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="34-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>7790笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="602774989212" data-nick="realme官方旗舰店" data-tnick="realme官方旗舰店" data-display="inline" data-atp="a!34-2,,,,,,,2200766936524"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="606547898634" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=606547898634&amp;skuId=4479628590028&amp;standard=1&amp;user_id=1695308781&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="35-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/TB1mSVEklr0gK0jSZFnkmTRRXXa_015138.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:373106502" class="proThumb-img " data-index="35:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN01VsSIR02LY1aqIohL7_!!3937219703.png_30x30.jpg" atpanel="35-1,606547898634,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:408254468" class="proThumb-img " data-index="35:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/3937219703/O1CN01vCVU1K2LY1anSjt9T_!!3937219703.png_30x30.jpg" atpanel="35-2,606547898634,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:6130517123" class="proThumb-img " data-index="35:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01Ep02Od2LY1aqtse6N_!!3937219703.png_30x30.jpg" atpanel="35-3,606547898634,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2299.00"><b>¥</b>2299.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=606547898634&amp;skuId=4479628590028&amp;standard=1&amp;user_id=1695308781&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Meizu/魅族 16T" data-p="35-11">Meizu/魅族 16T</a>

</div>
<div class="productShop" data-atp="b!35-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1695308781&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
魅族官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1386730924&amp;suid=d5f9d85f714d80f326b071bdc89360a9&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="35-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>7315笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="606547898634" data-nick="魅族官方旗舰店" data-tnick="魅族官方旗舰店" data-display="inline" data-atp="a!35-2,,,,,,,1695308781"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="601755994066" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=601755994066&amp;skuId=4420306794239&amp;standard=1&amp;user_id=2200766936524&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="36-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB12MygeYr1gK0jSZFDX1n9yVXa_013654.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:5566836922" class="proThumb-img " data-index="36:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/2200766936524/O1CN01aHlSD81y42UNRcnGZ_!!2200766936524.jpg_30x30.jpg" atpanel="36-1,601755994066,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5566921147" class="proThumb-img " data-index="36:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/2200766936524/O1CN01kuDDGK1y42UPeZlq9_!!2200766936524.jpg_30x30.jpg" atpanel="36-2,601755994066,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:619122369" class="proThumb-img " data-index="36:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/2200766936524/O1CN01sP4WNa1y42V3bs8e6_!!2200766936524.jpg_30x30.jpg" atpanel="36-3,601755994066,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="948.00"><b>¥</b>948.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=601755994066&amp;skuId=4420306794239&amp;standard=1&amp;user_id=2200766936524&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="realme Q" data-p="36-11">realme Q</a>

</div>
<div class="productShop" data-atp="b!36-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2200766936524&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
realme官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1319619242&amp;suid=d6d3363919b11e43d6600014627b7da5&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="36-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>8465笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="601755994066" data-nick="realme官方旗舰店" data-tnick="realme官方旗舰店" data-display="inline" data-atp="a!36-2,,,,,,,2200766936524"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="586594168121" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=586594168121&amp;skuId=4315843084120&amp;standard=1&amp;user_id=1659902905&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="37-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1rrySv4naK1RjSZFBLGoW7VXa_022422.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:2773625623" class="proThumb-img " data-index="37:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1_.Onv9rqK1RjSZK9ughyypXa_021438.jpg_30x30.jpg" atpanel="37-1,586594168121,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2774024001" class="proThumb-img " data-index="37:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1uW5vvYvpK1RjSZFqS4wXUVXa_021402.jpg_30x30.jpg" atpanel="37-2,586594168121,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2774024002" class="proThumb-img " data-index="37:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1tpSAv7zoK1RjSZFlNp9i4VXa_021408.jpg_30x30.jpg" atpanel="37-3,586594168121,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2774024005" class="proThumb-img " data-index="37:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1kGGAv3HqK1RjSZFkgft.WFXa_021427.jpg_30x30.jpg" atpanel="37-4,586594168121,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2774024006" class="proThumb-img " data-index="37:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1U2aqv4TpK1RjSZR0V6zEwXXa_021431.jpg_30x30.jpg" atpanel="37-5,586594168121,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:3160554748" class="proThumb-img " data-index="37:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i2/1659902905/O1CN01wvxYVd1XKX9tXFqDT_!!1659902905.png_30x30.jpg" atpanel="37-6,586594168121,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
  <b data-sku="1627207:3752388647" class="proThumb-img " data-index="37:7">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i4/1659902905/O1CN01fjXtfI1XKX9tXFAMK_!!1659902905.png_30x30.jpg" atpanel="37-7,586594168121,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
  <b data-sku="1627207:3752428173" class="proThumb-img " data-index="37:8">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i3/1659902905/O1CN0133nELq1XKX9syygud_!!1659902905.png_30x30.jpg" atpanel="37-8,586594168121,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
  <b data-sku="1627207:5584853645" class="proThumb-img " data-index="37:9">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i3/1659902905/O1CN01vXf1wc1XKX9uOn2Fn_!!1659902905.jpg_30x30.jpg" atpanel="37-9,586594168121,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">

<em title="1499.00"><b>¥</b>1499.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=586594168121&amp;skuId=4315843084120&amp;standard=1&amp;user_id=1659902905&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="4800万三摄 极点全面屏" data-p="37-11">HUAWEI Nova 4</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=586594168121&amp;skuId=4315843084120&amp;standard=1&amp;user_id=1659902905&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="4800万三摄 极点全面屏" data-p="37-11">4800万三摄 极点全面屏</a>

</div>
<div class="productShop" data-atp="b!37-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1659902905&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
久汇数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1125212165&amp;suid=7acea65a3902223db000aed1128680cd&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="37-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>688笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="586594168121" data-nick="久汇数码专营店" data-tnick="久汇数码专营店" data-display="inline" data-atp="a!37-2,,,,,,,1659902905"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="598358883934" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=598358883934&amp;skuId=4166937781561&amp;standard=1&amp;user_id=263726286&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="38-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1714128138/O1CN01XD6jbx29zFiy8gPmi_!!1714128138.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:458580214" class="proThumb-img " data-index="38:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1714128138/O1CN01RBSDW929zFiy9T9pq_!!1714128138.png_30x30.jpg" atpanel="38-1,598358883934,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1249.00"><b>¥</b>1249.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=598358883934&amp;skuId=4166937781561&amp;standard=1&amp;user_id=263726286&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Xiaomi/小米 小米CC 9E" data-p="38-11">Xiaomi/小米 小米CC 9E</a>

</div>
<div class="productShop" data-atp="b!38-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=263726286&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
能良数码官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1260604115&amp;suid=3104d9e75b70dd7765eb4cac087da498&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="38-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1740笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="598358883934" data-nick="能良数码官方旗舰店" data-tnick="能良数码官方旗舰店" data-display="inline" data-atp="a!38-2,,,,,,,263726286"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="589263619324" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=589263619324&amp;skuId=4057709249942&amp;standard=1&amp;user_id=2074230553&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="39-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1PUGie4iH3KVjSZPfDSNBiVXa_053747.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:131987527" class="proThumb-img " data-index="39:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB13n9pe8Kw3KVjSZFOil5rDVXa_053907.jpg_30x30.jpg" atpanel="39-1,589263619324,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2498.00"><b>¥</b>2498.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=589263619324&amp;skuId=4057709249942&amp;standard=1&amp;user_id=2074230553&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="4800万广角夜景三摄" data-p="39-11">vivo X27</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=589263619324&amp;skuId=4057709249942&amp;standard=1&amp;user_id=2074230553&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="4800万广角夜景三摄" data-p="39-11">4800万广角夜景三摄</a>

</div>
<div class="productShop" data-atp="b!39-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2074230553&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
vivo衡视专卖店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1168771290&amp;suid=a32e7718a6add4f9901ad4d8a073ad02&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="39-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1821笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="589263619324" data-nick="vivo衡视专卖店" data-tnick="vivo衡视专卖店" data-display="inline" data-atp="a!39-2,,,,,,,2074230553"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="600043598807" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=600043598807&amp;skuId=4435167038006&amp;standard=1&amp;user_id=682299517&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="40-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1pkN_dUT1gK0jSZFhwL5AtVXa_021920.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:422990506" class="proThumb-img " data-index="40:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1hIIQh5LaK1RjSZFx1vmmPFXa_030732.jpg_30x30.jpg" atpanel="40-1,600043598807,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4513375" class="proThumb-img " data-index="40:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1dSkrhVzqK1RjSZFvnu3B7VXa_030725.jpg_30x30.jpg" atpanel="40-2,600043598807,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5456959483" class="proThumb-img " data-index="40:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/3937219703/O1CN01u0uC5Z2LY1bACdNJB_!!3937219703.jpg_30x30.jpg" atpanel="40-3,600043598807,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5538347775" class="proThumb-img " data-index="40:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN01KvN6qa2LY1azIj2lf_!!3937219703.jpg_30x30.jpg" atpanel="40-4,600043598807,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="4099.00"><b>¥</b>4099.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=600043598807&amp;skuId=4435167038006&amp;standard=1&amp;user_id=682299517&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="7.2英寸大屏 5000mAh大电池" data-p="40-11">Huawei/华为 Mate 20 X</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=600043598807&amp;skuId=4435167038006&amp;standard=1&amp;user_id=682299517&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="7.2英寸大屏 5000mAh大电池" data-p="40-11">7.2英寸大屏 5000mAh大电池</a>

</div>
<div class="productShop" data-atp="b!40-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=682299517&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
旭翼数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1088971680&amp;suid=5183a4b5277c4fb46d4db628301cc01a&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="40-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>298笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="600043598807" data-nick="旭翼数码专营店" data-tnick="旭翼数码专营店" data-display="inline" data-atp="a!40-2,,,,,,,682299517"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="598661320133" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=598661320133&amp;skuId=4184333124391&amp;standard=1&amp;user_id=1710936647&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="41-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1LpnXbrY1gK0jSZTEimNDQVXa_104843.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="41:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/3937219703/O1CN01ACkfWd2LY1ZXzw84V_!!3937219703.jpg_30x30.jpg" atpanel="41-1,598661320133,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:441476440" class="proThumb-img " data-index="41:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1114511827/O1CN01Dg4upe1PMoAmd7pHS_!!1114511827.jpg_30x30.jpg" atpanel="41-2,598661320133,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:6565110" class="proThumb-img " data-index="41:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN0114thyL2LY1Zb2wjng_!!3937219703.jpg_30x30.jpg" atpanel="41-3,598661320133,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2049.00"><b>¥</b>2049.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=598661320133&amp;skuId=4184333124391&amp;standard=1&amp;user_id=1710936647&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="honor/荣耀 荣耀9X PRO" data-p="41-11">honor/荣耀 荣耀9X PRO</a>

</div>
<div class="productShop" data-atp="b!41-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1710936647&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
博盛景数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1276205832&amp;suid=3e509311ef765aebd6ad7b1f9fb81cee&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="41-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>9792笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="598661320133" data-nick="博盛景数码专营店" data-tnick="博盛景数码专营店" data-display="inline" data-atp="a!41-2,,,,,,,1710936647"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="569966140756" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=569966140756&amp;skuId=4263071097538&amp;standard=1&amp;user_id=1811831780&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="42-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB1TYU7swaTBuNjSszfDeXgfpXa_034348.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:75205313" class="proThumb-img " data-index="42:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/TB1w1.NsH9YBuNjy0FgUFExcXXa_031006.jpg_30x30.jpg" atpanel="42-1,569966140756,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:889626794" class="proThumb-img " data-index="42:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB1uIRZuYSYBuNjSspfdGkZCpXa_070720.jpg_30x30.jpg" atpanel="42-2,569966140756,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="999.00"><b>¥</b>999.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=569966140756&amp;skuId=4263071097538&amp;standard=1&amp;user_id=1811831780&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="我的智能摄影师" data-p="42-11">Meitu/美图 T9</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=569966140756&amp;skuId=4263071097538&amp;standard=1&amp;user_id=1811831780&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="我的智能摄影师" data-p="42-11">我的智能摄影师</a>

</div>
<div class="productShop" data-atp="b!42-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1811831780&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
美图旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=976441164&amp;suid=f1c9e5916d4a35faad9d565374504c2c&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="42-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3244笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="569966140756" data-nick="美图旗舰店" data-tnick="美图旗舰店" data-display="inline" data-atp="a!42-2,,,,,,,1811831780"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="599561201195" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=599561201195&amp;skuId=4392995482637&amp;standard=1&amp;user_id=1677335387&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="43-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB1kT9ucUz1gK0jSZLeFsP9kVXa_050044.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:52660871" class="proThumb-img " data-index="43:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1yL5UhQT2gK0jSZFk2QwIQFXa_043234.jpg_30x30.jpg" atpanel="43-1,599561201195,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2699.00"><b>¥</b>2699.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=599561201195&amp;skuId=4392995482637&amp;standard=1&amp;user_id=1677335387&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="【新品发布】nubia/努比亚 Z20年" data-p="43-11">nubia/努比亚 Z20</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=599561201195&amp;skuId=4392995482637&amp;standard=1&amp;user_id=1677335387&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="【新品发布】nubia/努比亚 Z20年" data-p="43-11">【新品发布】nubia/努比亚 Z20年</a>

</div>
<div class="productShop" data-atp="b!43-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1677335387&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
努比亚官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1288285250&amp;suid=5e673302a1279fd94dd212f7cea1eb51&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="43-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>565笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="599561201195" data-nick="努比亚官方旗舰店" data-tnick="努比亚官方旗舰店" data-display="inline" data-atp="a!43-2,,,,,,,1677335387"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="579623699524" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=579623699524&amp;skuId=4258112080186&amp;standard=1&amp;user_id=210910611&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="44-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/TB1XP4vIXzqK1RjSZFCrmLbxVXa_111249.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="44:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1ALAfhhYaK1RjSZFnETi80pXa_102212.jpg_30x30.jpg" atpanel="44-1,579623699524,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:507848351" class="proThumb-img " data-index="44:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1fUPZhgHqK1RjSZFPZfwwapXa_102214.jpg_30x30.jpg" atpanel="44-2,579623699524,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:86940080" class="proThumb-img " data-index="44:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/TB1NPP0hbrpK1RjSZTEle.WAVXa_102207.jpg_30x30.jpg" atpanel="44-3,579623699524,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1399.00"><b>¥</b>1399.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=579623699524&amp;skuId=4258112080186&amp;standard=1&amp;user_id=210910611&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="7.12英寸珍珠屏超高清分辨率" data-p="44-11">Huawei/华为 畅享 MAX</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=579623699524&amp;skuId=4258112080186&amp;standard=1&amp;user_id=210910611&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="7.12英寸珍珠屏超高清分辨率" data-p="44-11">7.12英寸珍珠屏超高清分辨率</a>

</div>
<div class="productShop" data-atp="b!44-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=210910611&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
晋商数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1086247068&amp;suid=416ab1b300dae4bb4ec59f47a3ee0cd6&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="44-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3175笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="579623699524" data-nick="晋商数码专营店" data-tnick="晋商数码专营店" data-display="inline" data-atp="a!44-2,,,,,,,210910611"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="590275747995" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=590275747995&amp;skuId=4474596622986&amp;standard=1&amp;user_id=1963544026&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="45-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB1mmO5MMHqK1RjSZFgC.17JXXa_122011.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1007902496" class="proThumb-img " data-index="45:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1ov2iMFYqK1RjSZLeDhDXppXa_020224.jpg_30x30.jpg" atpanel="45-1,590275747995,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2784408822" class="proThumb-img " data-index="45:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01rBFHC72LY1bpHcSzJ_!!3937219703.jpg_30x30.jpg" atpanel="45-2,590275747995,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2784408823" class="proThumb-img " data-index="45:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/3937219703/O1CN01baaw552LY1bthDl3P_!!3937219703.jpg_30x30.jpg" atpanel="45-3,590275747995,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2784408824" class="proThumb-img " data-index="45:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN01K2xXBY2LY1bqV40ZZ_!!3937219703.jpg_30x30.jpg" atpanel="45-4,590275747995,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:297498935" class="proThumb-img " data-index="45:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1FzzjMNTpK1RjSZFM.GDG_VXa_020240.jpg_30x30.jpg" atpanel="45-5,590275747995,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1088.00"><b>¥</b>1088.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=590275747995&amp;skuId=4474596622986&amp;standard=1&amp;user_id=1963544026&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="HUAWEI 华为畅享9S" data-p="45-11">HUAWEI 华为畅享9S</a>

</div>
<div class="productShop" data-atp="b!45-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1963544026&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
博海宇通数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1179377001&amp;suid=8ce2d34f5ffd172b8978b33a8398be30&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="45-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1.0万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="590275747995" data-nick="博海宇通数码专营店" data-tnick="博海宇通数码专营店" data-display="inline" data-atp="a!45-2,,,,,,,1963544026"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="606905979874" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=606905979874&amp;skuId=4261724213841&amp;standard=1&amp;user_id=2201415337596&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="46-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1XaV8bSzqK1RjSZPcCzbTepXa_113444.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:1105100035" class="proThumb-img " data-index="46:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1695308781/O1CN012EjkK4XmzK7HrHI_!!1695308781.jpg_30x30.jpg" atpanel="46-1,606905979874,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:1607142676" class="proThumb-img " data-index="46:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1695308781/O1CN012EjkK6ZjkG3aBVt_!!1695308781.jpg_30x30.jpg" atpanel="46-2,606905979874,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:307620976" class="proThumb-img " data-index="46:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1mTIScYvpK1RjSZFqrgwXUVXa_114244.jpg_30x30.jpg" atpanel="46-3,606905979874,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:387418020" class="proThumb-img " data-index="46:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1NIXBx7voK1RjSZPfz9dPKFXa_094127.jpg_30x30.jpg" atpanel="46-4,606905979874,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:514132218" class="proThumb-img " data-index="46:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1h0B.bMHqK1RjSZFEO.cGMXXa_113714.jpg_30x30.jpg" atpanel="46-5,606905979874,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1108.00"><b>¥</b>1108.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=606905979874&amp;skuId=4261724213841&amp;standard=1&amp;user_id=2201415337596&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="屏下光学指纹 索尼旗舰双摄" data-p="46-11">Meizu/魅族 16 x</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=606905979874&amp;skuId=4261724213841&amp;standard=1&amp;user_id=2201415337596&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="屏下光学指纹 索尼旗舰双摄" data-p="46-11">屏下光学指纹 索尼旗舰双摄</a>

</div>
<div class="productShop" data-atp="b!46-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2201415337596&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
连盛数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1056544091&amp;suid=151211822341c646b02d4f0804639a7a&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="46-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>2319笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="606905979874" data-nick="连盛数码专营店" data-tnick="连盛数码专营店" data-display="inline" data-atp="a!46-2,,,,,,,2201415337596"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="556565993453" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=556565993453&amp;skuId=4319584520584&amp;user_id=872196368&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="47-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1tmmaQVXXXXbMXXXXhxRX9VXX_045608.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:2584602592" class="proThumb-img " data-index="47:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01Unqszt2LY1cBdpZPK_!!3937219703.jpg_30x30.jpg" atpanel="47-1,556565993453,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:567863605" class="proThumb-img " data-index="47:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1nOOiaPnD8KJjSspbNWvbEXXa_110014.jpg_30x30.jpg" atpanel="47-2,556565993453,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7433570152" class="proThumb-img " data-index="47:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01tIhZSX2LY1cBdoUYq_!!3937219703.jpg_30x30.jpg" atpanel="47-3,556565993453,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1939.00"><b>¥</b>1939.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=556565993453&amp;skuId=4319584520584&amp;user_id=872196368&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="双摄变焦  骁龙835 6GB内存" data-p="47-11">Xiaomi/小米 小米6</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=556565993453&amp;skuId=4319584520584&amp;user_id=872196368&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="双摄变焦  骁龙835 6GB内存" data-p="47-11">双摄变焦  骁龙835 6GB内存</a>

</div>
<div class="productShop" data-atp="b!47-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=872196368&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
岸越数码专营店
</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>88笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="556565993453" data-nick="岸越数码专营店" data-tnick="岸越数码专营店" data-display="inline" data-atp="a!47-2,,,,,,,872196368"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="611706772953" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=611706772953&amp;skuId=4318368813285&amp;standard=1&amp;user_id=1715164541&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="48-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1CWk2xkY2gK0jSZFgaDI5OFXa_031205.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:3935615" class="proThumb-img " data-index="48:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/TB1c08axCf2gK0jSZFPWKJsopXa_045001.jpg_30x30.jpg" atpanel="48-1,611706772953,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:784482265" class="proThumb-img " data-index="48:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i6/TB1nnROy4n1gK0jSZKPEYhvUXXa_094538.jpg_30x30.jpg" atpanel="48-2,611706772953,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:96675050" class="proThumb-img " data-index="48:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1n58dxAT2gK0jSZFkTIIIQFXa_044639.jpg_30x30.jpg" atpanel="48-3,611706772953,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="5499.00"><b>¥</b>5499.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=611706772953&amp;skuId=4318368813285&amp;standard=1&amp;user_id=1715164541&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="OPPO Find X2" data-p="48-11">OPPO Find X2</a>

</div>
<div class="productShop" data-atp="b!48-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1715164541&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
OPPO欧曙专卖店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1519432661&amp;suid=f90dc027a198d821ba0de29af346c970&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="48-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>3479笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="611706772953" data-nick="oppo欧曙专卖店" data-tnick="oppo欧曙专卖店" data-display="inline" data-atp="a!48-2,,,,,,,1715164541"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="594817537179" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=594817537179&amp;skuId=4303555346577&amp;standard=1&amp;user_id=1695308781&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="49-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1695308781/O1CN01BB8uG52EjkO2VkK15_!!1695308781.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:12316641" class="proThumb-img " data-index="49:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/1695308781/O1CN0162EB952EjkO1MAJSQ_!!1695308781.jpg_30x30.jpg" atpanel="49-1,594817537179,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:281184419" class="proThumb-img " data-index="49:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1695308781/O1CN01sWRl1H2EjkO2EqLqr_!!1695308781.jpg_30x30.jpg" atpanel="49-2,594817537179,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:389306420" class="proThumb-img " data-index="49:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1695308781/O1CN01Q8seeO2EjkO3sPN7I_!!1695308781.jpg_30x30.jpg" atpanel="49-3,594817537179,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="1699.00"><b>¥</b>1699.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=594817537179&amp;skuId=4303555346577&amp;standard=1&amp;user_id=1695308781&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Meizu/魅族 16Xs" data-p="49-11">Meizu/魅族 16Xs</a>

</div>
<div class="productShop" data-atp="b!49-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1695308781&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
魅族官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1227449917&amp;suid=d5f9d85f714d80f326b071bdc89360a9&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="49-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>2505笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="594817537179" data-nick="魅族官方旗舰店" data-tnick="魅族官方旗舰店" data-display="inline" data-atp="a!49-2,,,,,,,1695308781"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="596887991598" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=596887991598&amp;skuId=4146437880323&amp;standard=1&amp;user_id=3063905773&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="50-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB1NB6bbAT2gK0jSZFk_PoIQFXa_112608.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:28328" class="proThumb-img " data-index="50:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/TB1.efJoiLaK1RjSZFx66qmPFXa_094402.jpg_30x30.jpg" atpanel="50-1,596887991598,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28338" class="proThumb-img " data-index="50:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i7/TB1vT_iobPpK1RjSZFFSg15PpXa_094423.jpg_30x30.jpg" atpanel="50-2,596887991598,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28341" class="proThumb-img " data-index="50:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/TB1p3jiogTqK1RjSZPhh7hfOFXa_094413.jpg_30x30.jpg" atpanel="50-3,596887991598,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="418.00"><b>¥</b>418.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=596887991598&amp;skuId=4146437880323&amp;standard=1&amp;user_id=3063905773&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="小巧全面屏 通话大音量" data-p="50-11">honor/荣耀 畅玩7</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=596887991598&amp;skuId=4146437880323&amp;standard=1&amp;user_id=3063905773&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="小巧全面屏 通话大音量" data-p="50-11">小巧全面屏 通话大音量</a>

</div>
<div class="productShop" data-atp="b!50-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=3063905773&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
创汇通达数码旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=973475716&amp;suid=fa730a1eb9c7db32e08bce1dda90249b&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="50-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>1560笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="596887991598" data-nick="创汇通达数码旗舰店" data-tnick="创汇通达数码旗舰店" data-display="inline" data-atp="a!50-2,,,,,,,3063905773"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="612436207834" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=612436207834&amp;skuId=4493250942429&amp;standard=1&amp;user_id=1637289231&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="51-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/TB1fSPLx7T2gK0jSZFkTEIIQFXa_022313.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:3542489537" class="proThumb-img " data-index="51:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/TB1Em.qwEY1gK0jSZFCL6UwqXXa_30x30.jpg" atpanel="51-1,612436207834,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:599016025" class="proThumb-img " data-index="51:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/TB1wMnNwp67gK0jSZPfL6ShhFXa_30x30.jpg" atpanel="51-2,612436207834,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7211759853" class="proThumb-img " data-index="51:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/TB12..qwEY1gK0jSZFCL6UwqXXa_30x30.jpg" atpanel="51-3,612436207834,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2298.00"><b>¥</b>2298.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=612436207834&amp;skuId=4493250942429&amp;standard=1&amp;user_id=1637289231&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="vivo Z6" data-p="51-11">vivo Z6</a>

</div>
<div class="productShop" data-atp="b!51-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1637289231&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
vivo欧曙专卖店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1513324790&amp;suid=49f7f4e70d8dfc4dd0bf5755d72022be&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="51-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>2.3万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="612436207834" data-nick="vivo欧曙专卖店" data-tnick="vivo欧曙专卖店" data-display="inline" data-atp="a!51-2,,,,,,,1637289231"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="606398801141" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=606398801141&amp;skuId=4423446599865&amp;user_id=1898764315&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="52-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i8/TB11kwwrv9TBuNjy0FcJ36eiFXa_093104.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:15782248" class="proThumb-img " data-index="52:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/3937219703/O1CN01wzIqwf2LY1axASCyH_!!3937219703.jpg_30x30.jpg" atpanel="52-1,606398801141,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28320" class="proThumb-img " data-index="52:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN013JKbyh2LY1awvnKSc_!!3937219703.jpg_30x30.jpg" atpanel="52-2,606398801141,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:28341" class="proThumb-img " data-index="52:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN01fQACbu2LY1b00Af81_!!3937219703.jpg_30x30.jpg" atpanel="52-3,606398801141,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="2399.00"><b>¥</b>2399.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=606398801141&amp;skuId=4423446599865&amp;user_id=1898764315&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="坚果手机 双卡双待" data-p="52-11">SMARTISAN/锤子 坚果pro</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=606398801141&amp;skuId=4423446599865&amp;user_id=1898764315&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="坚果手机 双卡双待" data-p="52-11">坚果手机 双卡双待</a>

</div>
<div class="productShop" data-atp="b!52-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=1898764315&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
金万吉数码专营店
</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>722笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="606398801141" data-nick="金万吉数码专营店" data-tnick="金万吉数码专营店" data-display="inline" data-atp="a!52-2,,,,,,,1898764315"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="612969202972" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=612969202972&amp;skuId=4318045949041&amp;standard=1&amp;user_id=2124152022&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="53-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/370627083/O1CN01pEHetz22C3v4H2KTp_!!370627083.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:135291939" class="proThumb-img " data-index="53:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/TB1YVpUv8v0gK0jSZKbL6TK2FXa_30x30.jpg" atpanel="53-1,612969202972,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:590396806" class="proThumb-img " data-index="53:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/TB1mUjWv8r0gK0jSZFnL6TRRXXa_30x30.jpg" atpanel="53-2,612969202972,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7202364793" class="proThumb-img " data-index="53:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/TB15wJWv7L0gK0jSZFxL6RWHVXa_30x30.jpg" atpanel="53-3,612969202972,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="13499.00"><b>¥</b>13499.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=612969202972&amp;skuId=4318045949041&amp;standard=1&amp;user_id=2124152022&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Samsung/三星 Galaxy Z Flip SM-F7000" data-p="53-11">Samsung/三星 Galaxy Z Flip SM-F7000</a>

</div>
<div class="productShop" data-atp="b!53-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2124152022&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
samsung佳酷专卖店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1531825725&amp;suid=1fc24b3cf450cdaf01b86e6cbb3c0d2f&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="53-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>2305笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="612969202972" data-nick="samsung佳酷专卖店" data-tnick="samsung佳酷专卖店" data-display="inline" data-atp="a!53-2,,,,,,,2124152022"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="612006017294" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=612006017294&amp;skuId=4307630412056&amp;standard=1&amp;user_id=197232874&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="54-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/TB1OoQuvAL0gK0jSZFA6GAA9pXa_100409.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:125164927" class="proThumb-img " data-index="54:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1714128138/O1CN01wxgxHW29zFlWewGju_!!1714128138.jpg_30x30.jpg" atpanel="54-1,612006017294,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:29645688" class="proThumb-img " data-index="54:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1714128138/O1CN019x5oyV29zFlfmAiXD_!!1714128138.jpg_30x30.jpg" atpanel="54-2,612006017294,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:463558165" class="proThumb-img " data-index="54:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1714128138/O1CN01f5tj2S29zFlWeuj8P_!!1714128138.jpg_30x30.jpg" atpanel="54-3,612006017294,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="4899.00"><b>¥</b>4899.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=612006017294&amp;skuId=4307630412056&amp;standard=1&amp;user_id=197232874&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Xiaomi/小米 小米10" data-p="54-11">Xiaomi/小米 小米10</a>

</div>
<div class="productShop" data-atp="b!54-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=197232874&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
绿森数码官方旗舰店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1526565904&amp;suid=4c11b25cd8d0f6140b8095a511f35f4f&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="54-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>4.0万笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="612006017294" data-nick="绿森数码官方旗舰店" data-tnick="绿森数码官方旗舰店" data-display="inline" data-atp="a!54-2,,,,,,,197232874"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="593305523406" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=593305523406&amp;skuId=4296912376489&amp;standard=1&amp;user_id=686947088&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="55-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i5/TB11Kzkfbr1gK0jSZFDk9j9yVXa_071328.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:3992641759" class="proThumb-img " data-index="55:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01FBq9022LY1bduopO6_!!3937219703.jpg_30x30.jpg" atpanel="55-1,593305523406,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4787301150" class="proThumb-img " data-index="55:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/3937219703/O1CN01D6kQl82LY1cBa7ue9_!!3937219703.jpg_30x30.jpg" atpanel="55-2,593305523406,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7401914301" class="proThumb-img " data-index="55:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN01GUo3YE2LY1c9SMRD7_!!3937219703.jpg_30x30.jpg" atpanel="55-3,593305523406,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="3499.00"><b>¥</b>3499.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=593305523406&amp;skuId=4296912376489&amp;standard=1&amp;user_id=686947088&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="nubia/努比亚 红魔" data-p="55-11">nubia/努比亚 红魔</a>

</div>
<div class="productShop" data-atp="b!55-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=686947088&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
卓瓦数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=959120869&amp;suid=6618e1838ed3ccc22fae4fa9b380efe0&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="55-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>114笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="593305523406" data-nick="卓瓦数码专营店" data-tnick="卓瓦数码专营店" data-display="inline" data-atp="a!55-2,,,,,,,686947088"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="611019059153" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=611019059153&amp;skuId=4465514218862&amp;user_id=725677994&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="56-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/725677994/O1CN01i85Ljm28vIjjGh2s1_!!725677994-0-sm.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:2499049911" class="proThumb-img " data-index="56:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/725677994/O1CN017UhUxp28vIjKQqtfO_!!725677994.jpg_30x30.jpg" atpanel="56-1,611019059153,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2503517872" class="proThumb-img " data-index="56:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/725677994/O1CN01WUcJqn28vIjLCIGXb_!!725677994.jpg_30x30.jpg" atpanel="56-2,611019059153,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:2519204060" class="proThumb-img " data-index="56:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/725677994/O1CN01PANr2K28vIjJYqd3s_!!725677994.jpg_30x30.jpg" atpanel="56-3,611019059153,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="6999.00"><b>¥</b>6999.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=611019059153&amp;skuId=4465514218862&amp;user_id=725677994&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Apple/苹果 Apple iPhone XS Max" data-p="56-11">Apple/苹果 Apple iPhone XS Max</a>

</div>
<div class="productShop" data-atp="b!56-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=725677994&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
天猫超市
</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>398笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="611019059153" data-nick="天猫超市" data-tnick="天猫超市" data-display="inline" data-atp="a!56-2,,,,,,,725677994"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="596864506699" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=596864506699&amp;skuId=4456064258629&amp;standard=1&amp;user_id=2201491547305&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="57-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1714128138/O1CN013Yykg129zFiMnqTAB_!!1714128138.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:4404456" class="proThumb-img " data-index="57:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1714128138/O1CN01X2kFYJ29zFiPK1wvk_!!1714128138.jpg_30x30.jpg" atpanel="57-1,596864506699,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:6032599172" class="proThumb-img " data-index="57:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01R6Q6EH2LY1bLtmKtR_!!3937219703.jpg_30x30.jpg" atpanel="57-2,596864506699,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:6032607156" class="proThumb-img " data-index="57:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/3937219703/O1CN01KJRxWD2LY1bTVTuEM_!!3937219703.jpg_30x30.jpg" atpanel="57-3,596864506699,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:66521134" class="proThumb-img " data-index="57:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1714128138/O1CN013Yykg129zFiMnqTAB_!!1714128138.jpg_30x30.jpg" atpanel="57-4,596864506699,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="3299.00"><b>¥</b>3299.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=596864506699&amp;skuId=4456064258629&amp;standard=1&amp;user_id=2201491547305&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Xiaomi/小米 Redmi K20 Pro" data-p="57-11">Xiaomi/小米 Redmi K20 Pro</a>

</div>
<div class="productShop" data-atp="b!57-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=2201491547305&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
君胜数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1231786827&amp;suid=001ea42b650c1fd44d92e2f039b2d68c&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="57-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>226笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="596864506699" data-nick="君胜数码专营店" data-tnick="君胜数码专营店" data-display="inline" data-atp="a!57-2,,,,,,,2201491547305"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="595109213375" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=595109213375&amp;skuId=4271584776283&amp;standard=1&amp;user_id=761647182&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="58-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/https://img.alicdn.com/bao/uploaded/i4/TB1SujJaBGE3KVjSZFhmdwkaFXa_104032.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:34749180" class="proThumb-img " data-index="58:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1714128138/O1CN01NbgYHT29zFiRPSwqg_!!1714128138.jpg_30x30.jpg" atpanel="58-1,595109213375,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:4404456" class="proThumb-img " data-index="58:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/1714128138/O1CN01X2kFYJ29zFiPK1wvk_!!1714128138.jpg_30x30.jpg" atpanel="58-2,595109213375,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5732244406" class="proThumb-img " data-index="58:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1714128138/O1CN01Alph0f29zFk0LSonp_!!1714128138.jpg_30x30.jpg" atpanel="58-3,595109213375,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5732280159" class="proThumb-img " data-index="58:4">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/1714128138/O1CN01MVlj3W29zFk7QZyNc_!!1714128138.jpg_30x30.jpg" atpanel="58-4,595109213375,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:5732286109" class="proThumb-img " data-index="58:5">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/1714128138/O1CN01ZL13jQ29zFk8B9ZEi_!!1714128138.jpg_30x30.jpg" atpanel="58-5,595109213375,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:66521134" class="proThumb-img " data-index="58:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i3/1714128138/O1CN013Yykg129zFiMnqTAB_!!1714128138.jpg_30x30.jpg" atpanel="58-6,595109213375,,,spu/shop,20,itemsku,"/>
 <i/>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">

<em title="3249.00"><b>¥</b>3249.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=595109213375&amp;skuId=4271584776283&amp;standard=1&amp;user_id=761647182&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="Xiaomi/小米 Redmi K20 骁龙 855" data-p="58-11">Xiaomi/小米 Redmi K20 骁龙 855</a>

</div>
<div class="productShop" data-atp="b!58-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=761647182&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
玩风数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1230367534&amp;suid=231237410afe747b9e6e61f215e10ddd&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="58-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>279笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="595109213375" data-nick="玩风数码专营店" data-tnick="玩风数码专营店" data-display="inline" data-atp="a!58-2,,,,,,,761647182"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="606524331004" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=606524331004&amp;skuId=4419661695126&amp;standard=1&amp;user_id=746181913&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="59-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/2815133273/O1CN01ePsjLC1a34rETtr6C_!!2815133273.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:311897035" class="proThumb-img " data-index="59:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2815133273/O1CN01VXC9tK1a34rQaYvtw_!!2815133273.jpg_30x30.jpg" atpanel="59-1,606524331004,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:3239184181" class="proThumb-img " data-index="59:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i1/2815133273/O1CN01P5VfRf1a34r6m7k11_!!2815133273.jpg_30x30.jpg" atpanel="59-2,606524331004,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:424596754" class="proThumb-img " data-index="59:3">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/2815133273/O1CN01Vkps7r1a34rFyR2O2_!!2815133273.jpg_30x30.jpg" atpanel="59-3,606524331004,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="599.00"><b>¥</b>599.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=606524331004&amp;skuId=4419661695126&amp;standard=1&amp;user_id=746181913&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="酷派COOL9双卡双待4G全网通手机" data-p="59-11">Coolpad/酷派 cool 9</a>
<a class="lightspot" href="//detail.tmall.com/item.htm?id=606524331004&amp;skuId=4419661695126&amp;standard=1&amp;user_id=746181913&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="酷派COOL9双卡双待4G全网通手机" data-p="59-11">酷派COOL9双卡双待4G全网通手机</a>

</div>
<div class="productShop" data-atp="b!59-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=746181913&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
锦万数码专营
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1232280736&amp;suid=7e9535901f93d6948eba3ef5d5b13ed6&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="59-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>2834笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="606524331004" data-nick="锦万数码专营" data-tnick="锦万数码专营" data-display="inline" data-atp="a!59-2,,,,,,,746181913"/>
</p>
 </div>

</div>
 
    

<div class="product  " data-id="601891568250" data-atp="a!,,1512,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
<a href="//detail.tmall.com/item.htm?id=601891568250&amp;skuId=4472817822219&amp;standard=1&amp;user_id=686947088&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" class="productImg" target="_blank" data-p="60-10">
<img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/TB1XRtSfhD1gK0jSZFy2wEiOVXa_070127.jpg" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
</a>
 
</div>

<div class="productThumb clearfix">
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:3992641759" class="proThumb-img " data-index="60:1">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i2/2200645849853/O1CN01IlqMiq2Mej0loTO6u_!!2200645849853.jpg_30x30.jpg" atpanel="60-1,601891568250,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
  <b data-sku="1627207:7386496015" class="proThumb-img " data-index="60:2">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i3/3937219703/O1CN01MjQ3ox2LY1c6LLG4v_!!3937219703.jpg_30x30.jpg" atpanel="60-2,601891568250,,,spu/shop,20,itemsku," src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
 <i/>
 </b>
</p>
</div>
</div>
  
 <p class="productPrice">

<em title="3499.00"><b>¥</b>3499.00</em>

 </p>

  <div class="productTitle productTitle-spu">

<!--product.spuTitleShow:true ,product.itemTitleShow:$product.itemTitleShow-->

<a href="//detail.tmall.com/item.htm?id=601891568250&amp;skuId=4472817822219&amp;standard=1&amp;user_id=686947088&amp;cat_id=2&amp;is_b=1&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" title="nubia/努比亚 NX629J" data-p="60-11">nubia/努比亚 NX629J</a>

</div>
<div class="productShop" data-atp="b!60-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=686947088&amp;rn=032b31e22ca2541dc3d92935018d8b3e&amp;keyword=智能手机" target="_blank">
卓瓦数码专营店
</a>
   <a href="//list.tmall.com/spu_detail.htm?fmtab=sp&amp;stype=search&amp;cat=2&amp;spuid=1210267668&amp;suid=6618e1838ed3ccc22fae4fa9b380efe0&amp;rn=032b31e22ca2541dc3d92935018d8b3e" target="_blank" class="productShop-num" atpanel="60-4,prop,,,,20,comboallitem,">等更多商家</a>
</div>
 <p class="productStatus">
<span>该款月成交 <em>329笔</em></span>
<span data-icon="small" class="ww-light ww-small m_wangwang J_WangWang" data-item="601891568250" data-nick="卓瓦数码专营店" data-tnick="卓瓦数码专营店" data-display="inline" data-atp="a!60-2,,,,,,,686947088"/>
</p>
 </div>

</div>
</div>
     
     <!--start PCSceneVideo -->
     <!--end PCSceneVideo -->
 
   
    
 
<div class="ui-page">
 <div class="ui-page-wrap">   <b class="ui-page-num">
   <b class="ui-page-prev">&lt;&lt;上一页</b>
                 <b class="ui-page-cur">1</b>
       <a href="?s=60&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;industryCatId=all&amp;type=pc#J_Filter" atpanel="2,,,,,20,footer,">2</a>
       <a href="?s=120&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;industryCatId=all&amp;type=pc#J_Filter" atpanel="2,,,,,20,footer,">3</a>
       <b class="ui-page-break">...</b>
     <a class="ui-page-next" href="?s=60&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;industryCatId=all&amp;type=pc#J_Filter" atpanel="2,pagedn,,,,20,footer,">下一页&gt;&gt;</a>
   </b>
 <b class="ui-page-skip">
 <form name="filterPageForm" method="get">
<input type="hidden" name="type" value="pc"/>
    <input type="hidden" name="q" value="智能手机"/>
         <input type="hidden" name="totalPage" value="80"/>
         <input type="hidden" name="sort" value="s"/><input type="hidden" name="style" value="g"/>    共80页，到第<input type="text" name="jumpto" class="ui-page-skipTo" size="3" value="1"/>页
 <button type="submit" class="ui-btn-s" atpanel="2,pageton,,,,20,footer,">确定</button>
 </form>
 </b>
 </div>
</div>

            <p class="relKeyRec relKeyRec-btm" data-spm="a220m.1000858.1000723" data-atp="{loc},{q},,,spu-key,5,key-bottom-s,">
 <span>您是不是想找</span>
             <a href="?vmarket=0&amp;frm=&amp;from=rs_1_key-bottom-s&amp;q=%BB%AA%CE%AA%CA%D6%BB%FA">华为手机</a>
               <a href="?vmarket=0&amp;frm=&amp;from=rs_1_key-bottom-s&amp;q=%D0%A1%C3%D7%CA%D6%BB%FA">小米手机</a>
               <a href="?vmarket=0&amp;frm=&amp;from=rs_1_key-bottom-s&amp;q=vivo%CA%D6%BB%FA">vivo手机</a>
               <a href="?vmarket=0&amp;frm=&amp;from=rs_1_key-bottom-s&amp;q=%C0%CF%C4%EA%CA%D6%BB%FA">老年手机</a>
               <a href="?vmarket=0&amp;frm=&amp;from=rs_1_key-bottom-s&amp;q=%BA%EC%C3%D7">红米</a>
               <a href="?vmarket=0&amp;frm=&amp;from=rs_1_key-bottom-s&amp;q=%D6%C7%C4%DC%D2%F4%CF%E4">智能音箱</a>
               <a href="?vmarket=0&amp;frm=&amp;from=rs_1_key-bottom-s&amp;q=%CA%D6%BB%FA%C6%BB%B9%FB">手机苹果</a>
               <a href="?vmarket=0&amp;frm=&amp;from=rs_1_key-bottom-s&amp;q=%D3%CE%CF%B7%CA%D6%BB%FA">游戏手机</a>
                             </p>
          
<div id="J_Recommend" class="recommend-loading" data-p4p-cfg="{'catid':'','keyword':'%D6%C7%C4%DC%CA%D6%BB%FA','propertyid':'','pid':'419108_1006','frontcatid':'','gprice':'0%2C100000000','loc':'','sort':'','sbid':'0','q2cused':'0','page':'1'}" data-atp="{idx},{itemid},,,p4p,1,p4p,">
<textarea class="ks-datalazyload"> &lt;script&gt;
(function(){com_TBCC=window.com_TBCC||{};com_TBCC.math=com_TBCC.math||{};com_TBCC.util=com_TBCC.util||{};com_TBCC.util.getCookie=function(A){var B=document.cookie.match("(?:^|;)\\s*"+A+"=([^;]*)");return B?unescape(B[1]):""};com_TBCC.util.getDoplotId=function(){var A=window.location.href.match(/_doplot_id=(\d+)/);if(A&amp;&amp;A[1]){return A[1]}};com_TBCC.util.getDoplots=function(A){var N=0;var B="";var K=8;function G(Z,U){Z[U&gt;&gt;5]|=128&lt;&lt;((U)%32);Z[(((U+64)&gt;&gt;&gt;9)&lt;&lt;4)+14]=U;var Y=1732584193;var X=-271733879;var W=-1732584194;var V=271733878;for(var R=0;R&lt;Z.length;R+=16){var T=Y;var S=X;var Q=W;var P=V;Y=J(Y,X,W,V,Z[R+0],7,-680876936);V=J(V,Y,X,W,Z[R+1],12,-389564586);W=J(W,V,Y,X,Z[R+2],17,606105819);X=J(X,W,V,Y,Z[R+3],22,-1044525330);Y=J(Y,X,W,V,Z[R+4],7,-176418897);V=J(V,Y,X,W,Z[R+5],12,1200080426);W=J(W,V,Y,X,Z[R+6],17,-1473231341);X=J(X,W,V,Y,Z[R+7],22,-45705983);Y=J(Y,X,W,V,Z[R+8],7,1770035416);V=J(V,Y,X,W,Z[R+9],12,-1958414417);W=J(W,V,Y,X,Z[R+10],17,-42063);X=J(X,W,V,Y,Z[R+11],22,-1990404162);Y=J(Y,X,W,V,Z[R+12],7,1804603682);V=J(V,Y,X,W,Z[R+13],12,-40341101);W=J(W,V,Y,X,Z[R+14],17,-1502002290);X=J(X,W,V,Y,Z[R+15],22,1236535329);Y=F(Y,X,W,V,Z[R+1],5,-165796510);V=F(V,Y,X,W,Z[R+6],9,-1069501632);W=F(W,V,Y,X,Z[R+11],14,643717713);X=F(X,W,V,Y,Z[R+0],20,-373897302);Y=F(Y,X,W,V,Z[R+5],5,-701558691);V=F(V,Y,X,W,Z[R+10],9,38016083);W=F(W,V,Y,X,Z[R+15],14,-660478335);X=F(X,W,V,Y,Z[R+4],20,-405537848);Y=F(Y,X,W,V,Z[R+9],5,568446438);V=F(V,Y,X,W,Z[R+14],9,-1019803690);W=F(W,V,Y,X,Z[R+3],14,-187363961);X=F(X,W,V,Y,Z[R+8],20,1163531501);Y=F(Y,X,W,V,Z[R+13],5,-1444681467);V=F(V,Y,X,W,Z[R+2],9,-51403784);W=F(W,V,Y,X,Z[R+7],14,1735328473);X=F(X,W,V,Y,Z[R+12],20,-1926607734);Y=M(Y,X,W,V,Z[R+5],4,-378558);V=M(V,Y,X,W,Z[R+8],11,-2022574463);W=M(W,V,Y,X,Z[R+11],16,1839030562);X=M(X,W,V,Y,Z[R+14],23,-35309556);Y=M(Y,X,W,V,Z[R+1],4,-1530992060);V=M(V,Y,X,W,Z[R+4],11,1272893353);W=M(W,V,Y,X,Z[R+7],16,-155497632);X=M(X,W,V,Y,Z[R+10],23,-1094730640);Y=M(Y,X,W,V,Z[R+13],4,681279174);V=M(V,Y,X,W,Z[R+0],11,-358537222);W=M(W,V,Y,X,Z[R+3],16,-722521979);X=M(X,W,V,Y,Z[R+6],23,76029189);Y=M(Y,X,W,V,Z[R+9],4,-640364487);V=M(V,Y,X,W,Z[R+12],11,-421815835);W=M(W,V,Y,X,Z[R+15],16,530742520);X=M(X,W,V,Y,Z[R+2],23,-995338651);Y=H(Y,X,W,V,Z[R+0],6,-198630844);V=H(V,Y,X,W,Z[R+7],10,1126891415);W=H(W,V,Y,X,Z[R+14],15,-1416354905);X=H(X,W,V,Y,Z[R+5],21,-57434055);Y=H(Y,X,W,V,Z[R+12],6,1700485571);V=H(V,Y,X,W,Z[R+3],10,-1894986606);W=H(W,V,Y,X,Z[R+10],15,-1051523);X=H(X,W,V,Y,Z[R+1],21,-2054922799);Y=H(Y,X,W,V,Z[R+8],6,1873313359);V=H(V,Y,X,W,Z[R+15],10,-30611744);W=H(W,V,Y,X,Z[R+6],15,-1560198380);X=H(X,W,V,Y,Z[R+13],21,1309151649);Y=H(Y,X,W,V,Z[R+4],6,-145523070);V=H(V,Y,X,W,Z[R+11],10,-1120210379);W=H(W,V,Y,X,Z[R+2],15,718787259);X=H(X,W,V,Y,Z[R+9],21,-343485551);Y=I(Y,T);X=I(X,S);W=I(W,Q);V=I(V,P)}return Array(Y,X,W,V)}function E(U,R,Q,P,T,S){return I(L(I(I(R,U),I(P,S)),T),Q)}function J(R,Q,V,U,P,T,S){return E((Q&amp;V)|((~Q)&amp;U),R,Q,P,T,S)}function F(R,Q,V,U,P,T,S){return E((Q&amp;U)|(V&amp;(~U)),R,Q,P,T,S)}function M(R,Q,V,U,P,T,S){return E(Q^V^U,R,Q,P,T,S)}function H(R,Q,V,U,P,T,S){return E(V^(Q|(~U)),R,Q,P,T,S)}function I(P,S){var R=(P&amp;65535)+(S&amp;65535);var Q=(P&gt;&gt;16)+(S&gt;&gt;16)+(R&gt;&gt;16);return(Q&lt;&lt;16)|(R&amp;65535)}function L(P,Q){return(P&lt;&lt;Q)|(P&gt;&gt;&gt;(32-Q))}function C(S){var R=Array();var P=(1&lt;&lt;K)-1;for(var Q=0;Q&lt;S.length*K;Q+=K){R[Q&gt;&gt;5]|=(S.charCodeAt(Q/K)&amp;P)&lt;&lt;(Q%32)}return R}function O(R){var Q=N?"0123456789ABCDEF":"0123456789abcdef";var S="";for(var P=0;P&lt;R.length*4;P++){S+=Q.charAt((R[P&gt;&gt;2]&gt;&gt;((P%4)*8+4))&amp;15)+Q.charAt((R[P&gt;&gt;2]&gt;&gt;((P%4)*8))&amp;15)}return S}com_TBCC.math.md5=function(P){return O(G(C(P),P.length*K))};com_TBCC.math.md5Test=function(){return com_TBCC.math.md5("abc")=="900150983cd24fb0d6963f7d28e17f72"};var A=com_TBCC.util.getCookie(A);var D;if(A){A=A.substr(0,11);if(window.location.href.indexOf("_doplot_id")&gt;-1){D=com_TBCC.util.getDoplotId()}else{D=parseInt(com_TBCC.math.md5(A).substr(0,8),16)%100}return D}}})();
(function () {
  window["_ent"] = []
  document.createElement("tbcc")
  var p4p_doplots = +com_TBCC.util.getDoplots('cna') || 0
  var J_Recommend = document.getElementById("J_Recommend")
  if(J_Recommend) {
    var cfgStr = J_Recommend.getAttribute("data-p4p-cfg")
    var cfg = eval("(" + cfgStr + ")")
    if(!cfg.frontcatid &amp;&amp; !cfg.catid &amp;&amp; !cfg.keyword){
      var q = (location.href.match(/(?:\?|&amp;)q=(.+?)(?:&amp;|$)/) || [])[1]
      var oq = (location.href.match(/(?:\?|&amp;)oq=(.+?)(?:&amp;|$)/) || [])[1]
      var cat = (location.href.match(/(?:\?|&amp;)cat=(.+?)(?:&amp;|$)/) || [])[1]
      if(q || oq) {
        J_Recommend.setAttribute("data-p4p-cfg", cfgStr.replace(",'keyword':'',", ",'keyword':'" + (q || oq) + "',"))
      }
      if(cat) {
        J_Recommend.setAttribute("data-p4p-cfg", cfgStr.replace(",'frontcatid':'',", ",'frontcatid':'" + cat + "',"))
      }
      var cfgStr = J_Recommend.getAttribute("data-p4p-cfg")
      var cfg = eval("(" + cfgStr + ")")
    }
    if(!cfg.frontcatid &amp;&amp; !cfg.catid &amp;&amp; !cfg.keyword){
      return
    }
  }
  if(p4p_doplots &gt;= 80 &amp;&amp; p4p_doplots &lt;= 1) {
    window.MBOX = {}
    MBOX.sendP4PError = function(){}
    KISSY.ready(function () {
      KISSY.use("ajax", function (S, IO) {
        var arg = {
          sbid: 2,
          frcatid: cfg.frontcatid,
          keyword: cfg.keyword,
          pid: cfg.pid,
          offset: (window.g_config.view === undefined ? 5 : [4, 5, 5][window.g_config.view]) * ((cfg.page || 1) - 1),
          propertyid: cfg.propertyid,
          gprice: cfg.gprice,
          loc: cfg.loc,
          sort: cfg.sort,
          feature_names: "promoPrice,multiImgs,tags,dsrDeliver,dsrDeliverGap,dsrDescribe,dsrDescribeGap,dsrService,dsrServiceGap"
        }
        var qs = ""
        for(var key in arg) {
          qs += key + "=" + arg[key] + "&amp;"
        }
        new IO({
          dataType: "jsonp",
          url: "//mbox.re.taobao.com/gt",
          data: {
            "pid": cfg.pid,
            "qs1": qs
          },
          jsonp: "cb",
          complete: function (data) {
            if(!data || data.rstCode) {
              arg["_input_charset"] = "GBK"
              data = {
                creation_path: "2015_4/129439",
                qs: [arg],
                template: "//acc.alicdn.com/tfscom/TB1nhBKHFXXXXa4XXXXdutXFXXX.js"
              }
            }
            var id = data.creation_path
            var $c = MBOX[id] = {}
            $c.data = data.data
            if(data.qs&amp;&amp;data.qs[0])data.qs[0].keyword = cfg.keyword
            $c.qs = data.qs || [arg]
            var uid = "c" + id.replace(/[^-a-z0-9]/ig, "-") + "-" + (+new Date());
            J_Recommend.innerHTML = '&lt;tbcc id="tbcc-c-' + uid + '" style="display:none"&gt;&lt;tbcc&gt;&lt;/tbcc&gt;&lt;/tbcc&gt;'
            KISSY.getScript(data.template.replace("http://strip.taobaocdn.com", "//acc.alicdn.com"), function () {
              _ent.use("cc/show", function (cc) {
                cc.show(id, uid)
              })
            })
          }
        })
      })
    })
  } else {
    var sbid = 1
    var id = "2016_8/131194"
    var script = "//acc.alicdn.com/tfscom/TB1XEs7RXXXXXXuXXXXXXXXXXXX.js"     
    var uid = "c" + id.replace(/[^-a-z0-9]/ig, "-") + "-" + (+new Date())
    J_Recommend.innerHTML = '&lt;tbcc id="tbcc-c-' + uid + '" data-args="?sbid=' + sbid + '" style="display:none"&gt;&lt;tbcc&gt;&lt;/tbcc&gt;&lt;/tbcc&gt;'
    KISSY.getScript(script, function(){
      _ent.use("cc/show", function (cc) {
        cc.show(id, uid).on("render", function(ds1){
          if (ds1.data.ds1.items.length == 0) {
            ds1.outerEle.style.display = "none"
          }
        })
      })
    })
  }
})()
&lt;/script&gt;
</textarea>
</div>
    
   <div class="btmSearch-loading" id="J_BtmSearch">
   <div class="btmSearch" data-spm="a220m.1000858.1000729">
<div class="btmSearch-main">
<form class="btmSearch-form clearfix" action="" target="_top" name="searchTop">
<fieldset>
<div class="btmSearch-input clearfix">
<input type="text" value="智能手机" autocomplete="off" tabindex="9" accesskey="s" class="btmSearch-mq" id="btm-mq" data-bts="0" name="q" aria-label="搜索关键词"/>
<button type="submit" class="ui-btn-search-l" aria-label="搜索">搜索<s/></button>
<input type="hidden" name="type" value="p"/>
<input type="hidden" name="redirect" value="notRedirect"/>
</div>
</fieldset>
</form>
</div>
</div>  </div>
   <p class="btmFeed">
 喵~在此反馈您的意见和建议吧，<a href="?q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;sort=s&amp;style=g&amp;industryCatId=all&amp;feedback=true" target="_blank">立刻反馈</a>
 </p>
 </div>
   <script>
 var __list_atpanel_param = "rn=032b31e22ca2541dc3d92935018d8b3e&amp;q=%D6%C7%C4%DC%CA%D6%BB%FA&amp;bid=0&amp;uid=&amp;catid=2&amp;prop=&amp;sort=s&amp;disp=g&amp;filter=&amp;loc=&amp;n=60&amp;page=1&amp;v=mall_1.0&amp;vmarket=0&amp;machineid=9e5ae2234826282e235e6ad1724d714b&amp;tmalltrackid=jx.tmall.com&amp;nav=&amp;navlog=&amp;rewq=%D6%C7%C4%DC%CA%D6%BB%FA&amp;rewcatid=2&amp;page_type=1&amp;stats=qp:1|cat:1|cat-qp:1|brand:1|brand-qp:1|F.itag:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0|key:1|pricemodel:auccount|pic:1|querytype:8|querytype:256|skuahead:1|brandlogo:1|spuPage:1|defaultsearch:1|spusort:1|app:tmallsearchquery|industryId:158|industryId:161|industryId:203|industryId:299|industryId:328|industryId:455|industryId:529|industryId:534|industryId:537|industryId:572|industryId:601|industryId:604|industryId:608|industryId:612|initiative:1&amp;filter_new=sort:s|post_fee:0|support_cod:0|manyPoints:0|wwonline:0|miaosha:0|isCombo:0|vip:0|pic_detail:0|floc:0|fprice:0|new:0|filter_mj:0&amp;from=&amp;active=0&amp;wq=&amp;suggest=&amp;search_type=search&amp;abtest=&amp;std_query=%D6%C7%C4%DC+%CA%D6%BB%FA&amp;top_query=&amp;direct_rc=2&amp;userid=&amp;cna=go4EF02jpQcCASrvLlMcZqHF&amp;",
 __header_atpanel_param = "bid=0&amp;rn=032b31e22ca2541dc3d92935018d8b3e";
</script>
  

 <script>
 var modsString = 'list/mods/srp/grid.js,list/mods/srp/cells/pin.js,list/mods/crumb/crumb.js,list/mods/attr/attr.js,list/atp2nav.js,list/mods/related/related.js,list/mods/filter/filter.js,list/mods/srp/cells/sku.js,list/mods/p4p/p4p.js';  var MODS = modsString.slice(0, modsString.length - 3).split('.js,');
</script>

<script>
 KISSY &amp;&amp; KISSY.ready(function(S){

 KISSY.use('dom', function (S, D) {
 var imglist = D.query('#J_NavAttrsForm img'),
 length = imglist.length,
 imgLoad = function (dom, callback) {
 var img = new Image();

 img.src = D.attr(dom, 'data-ks-lazyload');
 if (img.complete) {
 callback(dom);
 } else {
 img.onload = function () {
 callback(dom);
 img.onload = null;
 };
 }
 ;

 };
 if (length) {
 for (var i = 0; i &lt; length; i++) {
 imgLoad(imglist[i], function (dom) {
 dom.src = D.attr(dom, 'data-ks-lazyload');
 D.removeAttr(dom, 'data-ks-lazyload');
 D.show(dom);
 });
 }
 }
 });


 S.use(MODS+',list/core,list/init,list/pages/list,list/atp-v2,list/rn,list/filter,list/other,codetracker,datalazyload');

 var Win = window;
 var now = S.now();
 var timestamp = now - now%3600000;
 var appId = Win.g_config.appId;

 Win["UA_Opt"] = {
 LogVal : "UA_Val",
 MaxMCLog : 10,
 MaxKSLog : 10,
 MaxMPLog : 10,
 MaxFocusLog : 1,
 Token : new Date().getTime() + ":" + Math.random(),
 SendMethod : 8,
 Flag : 12430
 }
 Win["UA_Val"] = "";
 Win["getUA"] = function(){
 var tmp = Win["UA_Val"];
 UA_Opt.Token= new Date().getTime() + ":" + Math.random();
 UA_Opt.reload();
 return tmp;
 }

 S.getScript("//uaction.alicdn.com/js/ua.js?"+timestamp, function(){
 try{
 UA_Opt.Token = new Date().getTime() + ":" + Math.random();
 UA_Opt.reload();
 var uaexp=new Date();
 uaexp.setTime(uaexp.getTime()+30*24*60*60*1000);
 document.cookie="pnm_cku822="+encodeURIComponent(window.getUA())+";path=/;expires="+uaexp.toGMTString();
 }catch(err){}
 });
 });

</script>
<!--lidiB begin -->

<!--lidiB end -->
  </div>               <div id="footer" data-spm="a2226n1" class="tm-chn-3c-footer ">
   
   <div id="tmall-ensure">
   <style>
#footer { min-height: 475px; _height: 475px; }
#tmall-copyright .footer-copyright b { color: #fff; }
#tmall-ensure { background: url(//gw.alicdn.com/tfs/TB1ffDZhgMPMeJjy1XcXXXpppXa-1190-60.jpg) no-repeat; height: 60px; }
#tmall-ensure a { width: 296px; height: 60px; }
#tmall-copyright { border-color: #0061c4; background: #0061c4; }
#tmall-copyright .footer-copyright { background: #0061c4; color: #fff; }
#tmall-copyright .footer-copyright a { color: #fff; }
#server-num, #footer .server-num { background: #0061c4; color: #0061c4; }
@media (max-width: 1210px) {
    #tmall-ensure { background: url(//img.alicdn.com/tfs/TB15Bb9NpXXXXavXXXXXXXXXXXX-990-60.PNG) no-repeat; }
    #tmall-ensure a { width: 245px; }
}
</style>
<a class="c-shrh" href="//pages.tmall.com/wow/tmall-3c/act/north-serve?wh_service_id=2&amp;wh_default_id=0&amp;wh_isdetail=true&amp;wh_content_id=1"><span>预约配送 </span></a>
<a class="c-wythh" href="//pages.tmall.com/wow/tmall-3c/act/north-serve?wh_service_id=3&amp;wh_default_id=0&amp;wh_isdetail=true&amp;wh_content_id=1"><span>送货入户</span></a>
<a class="c-qglb" href="//pages.tmall.com/wow/tmall-3c/act/north-serve?wh_service_id=5&amp;wh_default_id=0&amp;wh_isdetail=true&amp;wh_content_id=2"><span>预约安装</span></a>
<a class="c-hpth" href="//pages.tmall.com/wow/tmall-3c/act/north-serve?wh_service_id=4&amp;wh_default_id=0&amp;wh_isdetail=true&amp;wh_content_id=2"><span>只换不修</span></a>
   </div>
   <div id="tmall-desc">
   <style>
.tmall-new-desc { background: url(//img.alicdn.com/tfs/TB1bFfkNFXXXXb5XFXXXXXXXXXX-120-180.PNG) 0 11px no-repeat; width: auto; padding: 0px 0 0 170px; margin: auto; height: 190px; }
#tmall-desc dl { width: 150px; }
#tmall-desc dl a { width: 120px; 
</style>
<div class="tmall-new-desc">
    <dl id="ensure">
        <dt><span>购物指南</span></dt>
        <dd>
            <a href="//register.tmall.com/" target="_blank">免费注册</a>
            <a href="https://www.alipay.com/user/reg_select.htm" target="_blank">开通支付宝</a>
            <a href="https://www.alipay.com/user/login.htm?goto=https%3A%2F%2Fwww.alipay.com%2Fuser%2Finpour_request.htm" target="_blank">支付宝充值</a>
        </dd>
    </dl>
    <dl id="beginner">
        <dt><span>电器城保障</span></dt>
        <dd>
            <a target="_blank" href="//pages.tmall.com/wow/tmall-3c/act/serve?spm=a222t.7836415.rdfw.1.qw1Y8h&amp;wh_isdetail=true&amp;wh_parent_id=0&amp;wh_id=0">花呗分期</a>
            <a target="_blank" href="//pages.tmall.com/wow/tmall-3c/act/serve?spm=a222t.7836415.rdfw.2.qw1Y8h&amp;wh_isdetail=true&amp;wh_parent_id=0&amp;wh_id=1">预约配送</a>
            <a target="_blank" href="//pages.tmall.com/wow/tmall-3c/act/serve?spm=a222t.7836415.rdfw.3.qw1Y8h&amp;wh_isdetail=true&amp;wh_parent_id=1&amp;wh_id=1">送货入户</a>
            <a target="_blank" href="//pages.tmall.com/wow/tmall-3c/act/serve?spm=a222t.7836415.rdfw.4.qw1Y8h&amp;wh_isdetail=true&amp;wh_parent_id=2&amp;wh_id=0">全国联保</a>
        </dd>
    </dl>
    <dl id="payment">
        <dt><span>支付方式</span></dt>
        <dd>
            <a href="//cshall.alipay.com/lab/help_detail.htm?help_id=245296" target="_blank">支付宝快捷支付</a>
            <a href="//cshall.alipay.com/lab/help_detail.htm?help_id=251547" target="_blank">支付宝余额付款</a>
            <a href="//cshall.alipay.com/lab/help_detail.htm?help_id=253912" target="_blank">支付宝钱包付款</a>
            <a href="http://cod.tmall.com" target="_blank">货到付款</a>
            <a href="http://abc.alipay.com/cool/fastPayment.htm" target="_blank">新人支付</a>
        </dd>
    </dl>
    <dl id="seller">
        <dt><span>商家服务</span></dt>
        <dd>
            <a target="_blank" href="//tmc.tmall.com/baoming/view_detail.htm?&amp;baomingConfigId=48201">入驻天猫电器城</a>
            <a target="_blank" href="//www.taobao.com/go/act/sale/serv-sale.php?ad_id=&amp;am_id=1301062135fb38745fdd&amp;cm_id=&amp;pm_id=">加入电器城服务保障</a>
            <a target="_blank" href="//maowo.tmall.com/">电器城喵言喵语圈子</a>
            <a target="_blank" href="//rule.tmall.com/tdetail-3183.htm?tag=self">电器城商家管理规范</a>
        </dd>
    </dl>
    <dl id="mobile">
        <dt>手机电器城</dt>
        <dd>
            <a href="//3c.tmall.com/" class="join"><img src="//img.alicdn.com/tps/i1/T1N64NFrxcXXb.IvUG-116-112.PNG" width="105" height="105" alt="手机天猫"/></a>
        </dd>
    </dl>
</div>
   </div>
 <div id="tmall-copyright">
 <div class="mui-global-fragment-load" data-fragment="tmbase/mui_footer_link"/>
 </div>
     <!-- global footer 2019 -->
   <div id="server-num">tmallsearch011019247044.center.na620</div>
</div>
</div>

</div>
<script type="text/javascript">(function(e){if(!e["_med"])e["_med"]={};var t=e["_med"];t.cookie=function(e,t,a){if(t!==undefined){a=a||{};if(typeof a.expires==="number"){var o=a.expires,l=a.expires=new Date;l.setTime(+l+o*864e5)}return document.cookie=[e,"=",String(t),a.expires?"; expires="+a.expires.toUTCString():"",a.path?"; path="+a.path:"",a.domain?"; domain="+a.domain:"",a.secure?"; secure":""].join("")}var r=e?undefined:{};var i=document.cookie?document.cookie.split("; "):[];for(var n=0,s=i.length;n&lt;s;n++){var b=i[n].split("=");var d=b.shift();var p=b.join("=");if(e&amp;&amp;e===d){r=p;break}if(!e&amp;&amp;p!==undefined){r[d]=p}}return r};var a=document;var o=e.devicePixelRatio||1,l=a.documentElement.clientWidth,r=a.documentElement.clientHeight,i,n,s,b=/initial-scale=([\d\.]+?),/i,d,p;if(a.querySelector){p=a.querySelector('meta[name="viewport"]');if(p){d=b.exec(p.content+",");if(d){s=parseFloat(d[1],10)}}}if(s){l=l*s;r=r*s}if(screen){if(Math.abs(screen.width-l*o)&lt;.2*screen.width){l=screen.width/o;r=screen.height/o;i=screen.width;n=screen.height}else{l=screen.width;r=screen.height;i=screen.width*o;n=screen.height*o}}else{i=l*o;n=r*o}var m="createTouch"in a&amp;&amp;"ontouchstart"in e?1:0;var c=["dw:"+l,"dh:"+r,"pw:"+i,"ph:"+n,"ist:"+m].join("&amp;");t.cookie("_med",c,{expires:3650})})(window);</script>

<span id="J_MuiTempleSpan1585291395435" style="display: block; font-size: 42px; position: absolute; top: 0px; left: 0px; visibility: hidden; width: auto; height: auto; margin: 0px; padding: 0px; font-variant: normal; font-family: tm-list-font;">&amp;#xf0002;</span></body></HTML>

"""
from pyquery import PyQuery as pq
import re
doc=pq(html)
#print(doc.find('#J_ItemList'))
k = doc('.product .productImg-wrap ').items()  # 从html文件中过滤符合条件的内容，返回的是列表形式
for i in k:
    k = i('a').attr('href')  # 获取a标签中的链接，即店铺链接
    print(k)
    nk = re.findall('id=(.*?)&.*?&user_id=(.*?)&', k)  # 获取商品ID与店铺卖家ID，用于后面拼接
    URL = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + nk[0][0] + '&sellerId=' + nk[0][
        1] + '&currentPage=1'  # 拼接店铺商品的评价链接

    # productshoplink.append(URL)  # 添加到商品链接的列表中