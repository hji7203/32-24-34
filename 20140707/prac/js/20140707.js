$(document).ready(function(){
	$('#myModal').click(function(){
		$('#myModal').modal();
	});

	
	$('li').hover(function(){
		
		$(this).css("background-color","#fdffdc");
	},function(){
		$(this).css("background-color","pink");
	});


	$("#wldls").click(function(){
		$("#div1").fadeIn();
		$("#div2").fadeIn("slow");
		$("#div3").fadeIn(3000);
	});


	$('#div1').click(function(){
		$("#div1").animate({
			left:'250px',
			opacity:'0.5',
			height:'150px',
			width:'1280px'
		});

	});

	$('#div2').click(function(){
		$("#div2").animate({
			left:'250px',
			opacity:'0.5',
			height:'150px',
			width:'1280px'
		});
	});


	$('#div3').click(function(){
		$("#div3").animate({
			left:'250px',
			opacity:'0.5',
			height:'150px',
			width:'1280px'
		});
	});

	$('.btn-danger').click(function(){
		$('.btn-danger').popover('toggle');

	});
	console.log($('#example1'));
	$('#example1').arctext({radius: 400});
	$('#example4').arctext({radius: 300});
	$('#example4').on('click', function() {
		$('example4').arctext('set', {
			radius		: 300, 
			dir			: -1,
			animation	: {
				speed	: 300,
				easing  : 'ease-out'
			}
		});
	});
});