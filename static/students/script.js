

function GenerateCoursesHTML(data) {
   html = geneList(data);
   document.getElementById("list").innerHTML = html;
}

function goBack() {
    window.history.back();
}

// function loginFailed() {
//    console.log(document.referrer);
//    console.log("fuck");
//    document.getElementById("1").innerHTML = "The username and password were incorrect";
// }

