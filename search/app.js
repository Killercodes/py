
function Populate(repoPath,folderName)
{
    (async () => {
        const response = await fetch("https://api.github.com/repos/"+repoPath+"/contents/" + folderName);
        const data = await response.json();
        let htmlString = '';

        var table2 = document.getElementById("tsearch");

        var repoName = repoPath.split('/')[1]

        for (let file of data) 
        {
            var actualpath= "https://killercodes.github.io/"+repoName+"/" + file.path;
            var fileName = (file.path).replace(".md","");
            htmlString = `<a href="${fileName}" target="IFcontent">${file.name}</a>`;
            var row2 = table2.insertRow(-1);
            var cell2 = row2.insertCell(0);
            cell2.innerHTML = htmlString;
        }

    })()
}

function mySearch() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("tsearch");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
