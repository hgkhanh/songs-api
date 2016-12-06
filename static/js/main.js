$(document).ready(function() {
	$('.btn.meta-btn ').click(function(){
		var song_id = $(this).attr('data-song-id');
		postClickedMeta(song_id);
	});
});

function postClickedMeta(id) {
	$.ajax({
		method: 'POST',
		url: 'songs/'+id+'/meta'
	})
	.done(function(data){
		getClickedMeta(id);
	});
}

function getClickedMeta(id) {
	$.ajax({
		method: 'GET',
		url: 'songs/'+id+'/meta'
	})
	.done(function(data){
		json_data = JSON.parse(data);
		if(json_data["Clicked"] == true) {
			$('#badge-'+id).text("True");
		}
	});
}