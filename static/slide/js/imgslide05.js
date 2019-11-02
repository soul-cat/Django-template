$.fn.picslide05 = function () {
    var imgslid = $(this);

    var li = imgslid.find("ul.content li").size(); //统计多少张图片
    var li_width = imgslid.find(".slides ul.frame li").width(); //获取img的宽度
    imgslid.find(".slides ul.frame").width(li_width * 3); //设置宽度

    var i_old = 0; //当前的编号
    var i_new = 0; //当前的编号
    var direction = "next" //

    imgslid.find(".slides ul.frame li").eq(1).html(imgslid.find("ul.content li").eq(0).html());
    imgslid.find("div.title a").html(imgslid.find("ul.content li").eq(0).find("img").attr("alt"));
    imgslid.find("div.title a").attr("href", imgslid.find("ul.content li").eq(0).find("a").attr("href"));


    imgslid.find("div.slides").scrollLeft(li_width);

    imgslid.find("div.next").hover(function () { $(this).addClass("on"); }, function () { $(this).removeClass("on") });

    imgslid.find("div.next").click(function () {
        i_new++;
        i_new = i_new % li;
        direction = "next";
        showpic();

    });

    imgslid.find("div.pre").hover(function () { $(this).addClass("on"); }, function () { $(this).removeClass("on") });
    imgslid.find("div.pre").click(function () {
        if (i_new == 0)
            i_new = 4;
        else
            i_new--;

        direction = "pre"
        showpic();
    });

    function showpic() {
        if (i_old == i_new) return;

        if (direction == "next") {
            imgslid.find(".slides ul.frame li").eq(2).html(imgslid.find("ul.content li").eq(i_new).html());
            imgslid.find("div.slides").animate({ scrollLeft: li_width * 2 }, "normal", function () { imgslid.find(".slides ul.frame li").eq(1).html(imgslid.find("ul.content li").eq(i_new).html()); imgslid.find("div.slides").scrollLeft(li_width); }); //图片移动

        }
        else {
            imgslid.find(".slides ul.frame li").eq(0).html(imgslid.find("ul.content li").eq(i_new).html());
            imgslid.find("div.slides").animate({ scrollLeft: 0 }, "normal", function () { imgslid.find(".slides ul.frame li").eq(1).html(imgslid.find("ul.content li").eq(i_new).html()); imgslid.find("div.slides").scrollLeft(li_width); }); //图片移动

        };
        imgslid.find("ul.pointer li.on").removeClass("on");
        imgslid.find("ul.pointer li").eq(i_new).addClass("on");

        imgslid.find("div.title a").html(imgslid.find("ul.content li").eq(i_new).find("img").attr("alt"));
        imgslid.find("div.title a").attr("href", imgslid.find("ul.content li").eq(i_new).find("a").attr("href"));

        i_old = i_new;
    };

    imgslid.find("ul.pointer li").each(function (i) {
        //生成按钮点击事件
        $(this).click(function () {
            i_new = i;
            if (i_old < i_new)
                direction = "next";
            else
                direction = "pre";
            showpic();
        });
    });

    function tt() {//定时器函数
        i_new++;
        i_new = i_new % li;
        direction = "next";
        showpic();
    };
    var t = setInterval(tt, 3000); //定时器
    imgslid.hover(function () { clearInterval(t); }, function () { t = setInterval(tt, 3000); });


};
