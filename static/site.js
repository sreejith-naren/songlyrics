function main() {
    $.get({url:'http://127.0.0.1:5000/artist', success:(data)=>{
        list= '';
        data.forEach(element => {
        list += '<li>'+ element.name + '</li>';
        });

        tag= `<ul>${list}</ul>`;
        $('div.artistlist').html(tag);
    },
    });
}

$(main);