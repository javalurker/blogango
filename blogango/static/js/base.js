﻿jQuery.cookie=function(e,t,n){if(typeof t=="undefined"){var a=null;if(document.cookie&&document.cookie!=""){var f=document.cookie.split(";");for(var l=0;l<f.length;l++){var c=jQuery.trim(f[l]);if(c.substring(0,e.length+1)==e+"="){a=decodeURIComponent(c.substring(e.length+1));break}}}return a}n=n||{},t===null&&(t="",n.expires=-1);var r="";if(n.expires&&(typeof n.expires=="number"||n.expires.toUTCString)){var i;typeof n.expires=="number"?(i=new Date,i.setTime(i.getTime()+n.expires*24*60*60*1e3)):i=n.expires,r="; expires="+i.toUTCString()}var s=n.path?"; path="+n.path:"",o=n.domain?"; domain="+n.domain:"",u=n.secure?"; secure":"";document.cookie=[e,"=",encodeURIComponent(t),r,s,o,u].join("")};var close_reply,del_confirm,reply,toggleNav,_bdhmProtocol;$(function(){return $('input[name="q"]').eq(1).focus(function(){return $("div.headernav span:first").removeClass(),$('input[name="q"]').eq(1).removeClass(),$("div.headernav span:first").addClass("input"),$('input[name="q"]').eq(1).addClass("input")}),$('input[name="q"]').eq(1).blur(function(){$("div.headernav span:first").removeClass("input"),$('input[name="q"]').eq(1).removeClass("input");if($('input[name="q"]').eq(1).val()!=="")return $("div.headernav span:first").addClass("exists"),$('input[name="q"]').eq(1).addClass("exists")})}),$(window).load(function(){return $.get("/static/img/search-exists.jpg"),$.get("/static/img/search-input.jpg")}),toggleNav=function(e){var t,n,r,i,s,o,u;s=["category","months","links"],$("."+e+":eq(0)").stop();for(i=o=0,u=s.length-1;0<=u?o<=u:o>=u;i=0<=u?++o:--o)$("."+s[i]+":eq(0)").css("top")!=="-3000px"&&(r=$("."+s[i]+":eq(0)").height(),n=s[i],$("."+s[i]+":eq(0)").animate({top:"-"+(r-40)+"px"},t=function(e){return function(){return $("."+e+":eq(0)").css({top:"-3000px"})}}(n)));if($("."+e+":eq(0)").css("top")==="-3000px")return r=$("."+e+":eq(0)").height(),$("."+e+":eq(0)").css({top:"-"+(r-40)+"px"}),$("."+e+":eq(0)").animate({top:"40px"})},del_confirm=function(e){if(!confirm("是否删除id为"+e+"的文章"))return!1},reply=function(e,t){var n;return n=$("#comment_form").clone(),$("#comment_form").detach(),$("#comment-"+t).after(n),$("#comment_form input[name=index]").eq(0).val(e),$("#comment_form").append('<a href="javascript:close_reply()">关闭</a>')},close_reply=function(){var e;return $("#comment_form a").eq(0).detach(),e=$("#comment_form").clone(),$("#comment_form").detach(),$("div.article").append(e),$("#comment_form input[name=index]").eq(0).val(-1)},_bdhmProtocol="https:"===document.location.protocol?" https://":" http://",document.write(unescape("%3Cscript src='"+_bdhmProtocol+"hm.baidu.com/h.js%3F35e3e826c18b903de353ce54647c8ba4' type='text/javascript'%3E%3C/script%3E"));