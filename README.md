# leetcode_scraper_and_pdf
A leetcode scraper to compile all questions in leetcode free tier to text file. pdf also available. 



# if new questions get added, run again to get new questions.


Open google chrome, navigate to leetcode problems page
click on inspect, navigate to dev console and paste the commands below.
copy question links and paste in text file named question_links.txt
go to next page and repeat till you have all the questions links.
put python script and question link file in same folder.
run and wait to compile to text file, the convert to pdf online.

var x = document.querySelectorAll("a");
var myarray = []
for (var i=0; i<x.length; i++){
  if(x[i].getAttribute('href').indexOf('problem') > -1 && x[i].getAttribute('href').indexOf('solution') == -1 )
  {
  var cleanlink = x[i].href;
  myarray.push([cleanlink]);
  }
};
function make_table() {
    var table = '<table><thead><th>Links</th></thead><tbody>';
   for (var i=0; i<myarray.length; i++) {
            table += '<tr><td>'+ myarray[i][0] ;
    };

    var w = window.open("");
w.document.write(table);
}
make_table()
