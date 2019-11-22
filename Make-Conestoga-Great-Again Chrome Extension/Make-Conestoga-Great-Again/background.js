
var classes = document.getElementsByClassName("DailyShowCourse");


function format_time(str){
  first = str.slice(0, str.length/2);
  last = str.slice(str.length/2);
  return final = first + ":" + last;
}

for (var i = 0; i<classes.length;i++){
  cls = classes[i].id;
  //console.log(cls);

  duration = classes[i].getAttribute("rowspan");
  //console.log(duration);

  cls_duration = parseInt(duration) * 15 / 60 * 100;
  //console.log(cls_duration);

  var class_begin_time = classes[i].parentNode.id;

  var class_end_time = parseInt(class_begin_time) + parseInt(cls_duration);

  var class_time = format_time(String(class_begin_time)) +
                  " - " + 
                  format_time(String(class_end_time));

  var breaks = document.createElement("br");
  var result = document.createTextNode(class_time);
  classes[i].firstElementChild.appendChild(breaks);
  classes[i].firstElementChild.appendChild(result);
}