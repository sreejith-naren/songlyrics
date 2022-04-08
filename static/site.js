function main() {
    $.get({url:'http://127.0.0.1:5000/artist', success:(data)=>{
        list= '';
        data.forEach(element => {
        list += `<li class="artist" value=${element.id}>`+ element.name + `</li>`;
        });

        tag= `<ul>${list}</ul>`;
        $('div.artistlist').html(tag);
    },
    });
}
$(document).on('click', 'li.artist', function () {
    $.get({
      url: `http://127.0.0.1:5000/songs/${this.value}`,
      success: (data) => {
        list = '';
        data.forEach((element) => {
          list +=
            `<li class="songbox" id=${element.song_id}>` +
            element.song_name +
            `</li>`;
        });
        tag = `<ul type="none">${list}</ul>`;
        $('div.songlist').html(tag);
        console.log(data);
      },
    });
  });

  $(document).on('click', 'li.songbox', function () {
    $.get({
      url: `http://127.0.0.1:5000/songs/${this.value}/lyrics/${this.id}`,
      success: (data) => {
        lyrics = `<h4 class="lhead">Lyrics</h4><pre><p>${data}</p></pre>`;
        $('div.lyrics').html(lyrics);
      },
    });
  });  
$(main);