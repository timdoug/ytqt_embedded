$.get('http://localhost:5000', {'url': document.URL}, function(vid_url) {
    $('div#player-api').replaceWith('<div class="player-width player-height off-screen-target watch-content player-api" style="overflow: hidden; "><video src="' + vid_url + '" width="640" height="390" controls autoplay>Loading video...</video></div>');
});

