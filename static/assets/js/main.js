jQuery(document).ready(function(){
	
	$(".filter").click(function(){
				var value = $(this).attr("data-filter")
				if (value == "all")
					{
						$(".category").show("1000");
					}
				else
				{
					$(".category").not("."+value).hide("1000");
					$(".category").filter("."+value).show("1000");
				}
				$("ul .filter").click(function(){
					$(this).addClass('filter-active').siblings().removeClass('filter-active');
				})
	})
			

	
	if( $('.cd-stretchy-nav').length > 0 ) {
		var stretchyNavs = $('.cd-stretchy-nav');
		
		stretchyNavs.each(function(){
			var stretchyNav = $(this),
				stretchyNavTrigger = stretchyNav.find('.cd-nav-trigger');
			
			stretchyNavTrigger.on('click', function(event){
				event.preventDefault();
				stretchyNav.toggleClass('nav-is-visible');
			});
		});

		$(document).on('click', function(event){
			( !$(event.target).is('.cd-nav-trigger') && !$(event.target).is('.cd-nav-trigger span') ) && stretchyNavs.removeClass('nav-is-visible');
		});
	}
	
});