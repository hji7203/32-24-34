$(document).ready(function(){
	$('idea1.html')
	$('#sidebar > ul.nav > li').hover(function(){
		$(this).css("background-color","rgba(255,255,255,0.8)");
	},function(){
		$(this).css("background-color","rgba(255,255,255,0)");
	});
	$('#style_div > div > div > h3').hover(function(){
		$(this).css("color","#536200");
	},function(){
		$(this).css("color","#000000");
	});
	$("div#container > h3").click(function(){
		if ($("#div#banner_fade").css('width') == '600px'){
			$("#div#banner_fade").animate({
				width: '0px',
				height:'0px'

			});
		}else{
			$("#div#banner_fade").animate({
				width: '600px',
				height:'400px'
			});
		}
	});	

})