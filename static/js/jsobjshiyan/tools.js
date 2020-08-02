//创建新DIV
class CreateDiv{
    constructor(id,btnid,text,editor){
        this.oDiv = document.getElementById(id);
        this.oBtn = document.getElementById(btnid);
        //textarea必须通过class来获取
        this.textDiv = document.getElementsByClassName(text);
        this.editor = editor;
        var _this = this;
        this.count = 0;
        this.oBtn.onclick = function (){
            _this.functOnClick(this);
        };
    }

    //点击提交按钮后的响应函数
    functOnClick(bTnthis){
        //从textarea获取text
        //var text = this.textDiv.value;
        //从editor获取text
        var text = this.editor.txt.html();
        this.createNewDiv(text,false);
        //输入内容提交后重新清空输入栏
        this.editor.txt.html('')
    }

    //网页为首次加载，加载服务器数据库内容创建系列div,若网页为非首次加载，则根据editor内容发送ajx请求并本地创建一个新div
    createNewDiv(text,initial){
        var newDiv = document.createElement('div');
        //newDiv.style.height = '100px';
        newDiv.style.borderBottomStyle = 'solid';
        newDiv.style.borderRadius = '7px';
        if (!initial){
            var Reg = /(\n\r|\r\n|\r|\n)/g;
            var t =text.replace(Reg,'<br/>');
            t = t + '<br />' + '修改时间：'+ this.getDateMsg();
            newDiv.innerHTML = t;   //获取输入内容
            //this.count = this.oDiv.getElementsByTagName('div').length;       //获取div个数，给数据库主键赋值
            this.textDiv.value = '';
            this.sendPost(t);
        }
        else {
            newDiv.innerHTML = text;
        }
        this.oDiv.appendChild(newDiv);
    }
    
    //发送ajx请求
    sendPost(str){
        var config={};
        var ajx=new XMLHttpRequest();
        var url = window.location.href;
        ajx.open('post',url,true);
        //ajx.open('post','http://118.126.112.81/map/',true);
        ajx.setRequestHeader('content-type','application/x-www-form-urlencoded');
        //普通django的post方式
        //str = `text=${str}&id=${this.count}`;
        var jobj = {text:str,id:''+this.count};
        str = JSON.stringify(jobj);
        ajx.send(str);
        ajx.onreadystatechange == function(){
            this.dealWithResponse()
        }

    }
    dealWithResponse(){
        alert('recieve data');
    }
    getDateMsg(){
        var d = new Date();
        var day = d.getDate();
        var year = d.getFullYear();
        var mon = d.getMonth();
        var h = d.getHours();
        var min = d.getMinutes();
        if(parseInt(min)<10){
            min = '0'+min;
        }
        var sec = d.getSeconds();
        if(parseInt(sec)<10){
            sec = '0'+sec;
        }
        var dateinfo = `${year}年${mon+1}月${day}日${h}:${min}:${sec}`;
        return dateinfo;
    }
}
//第一次进入页面加载数据库内容
function loadServerData(creatDiv) {
    var ajx= new XMLHttpRequest();
    var url = window.location.href;
    ajx.open('post',url,true);
    //ajx.open('post','http://118.126.112.81/map/',true);
    ajx.setRequestHeader('content-type','application/x-www-form-urlencoded');
    ajx.send(`load=yes`);
    ajx.onreadystatechange = function () {
        if (ajx.readyState==4)
        {
            var arr = dealWithJson(ajx.responseText);
            for (var text of arr){
                creatDiv.createNewDiv(text,true);
            }
        }
    }
}
function dealWithJson(str) {
    arr = new Array();
    str = JSON.parse(str);
    for (var index in str){
        arr.push(str[index]['fields']['Wtext']);
    }
    return arr;
}

