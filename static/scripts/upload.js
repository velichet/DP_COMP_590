// ITERATING OVER THE FORM

function form() {
    // Get form
    var form = document.forms.dataInput

    var local = window.location.pathname.includes("local")
    // Create object to hold form data
    var obj = {
        "title": form.datasetTitle.value,
        "description": form.datasetDesc.value,
        "local": local
    }

    // Current field key
    var currFKey;
    // Statistics object
    var stats = {};
    // Get remaining form data
    for(var i=0; i< form.elements.length; i++ ) {
        var fieldName = form.elements[i].name;
        var fieldValue = form.elements[i].value;
        // console.log(fieldName + ": " + fieldValue)

        if (fieldName === "col_name") {
            currFKey = fieldValue;
            stats[currFKey] = {}
        }

        var stat = {}
        if (fieldName === "stat_choice") {
            stat[fieldValue] = {
                "epsilon": form.elements[i + 1].value,
                "low": form.elements[i + 2].value,
                "high": form.elements[i + 3].value
            }
            i+=3;
            stats[currFKey] = Object.assign(stat, stats[currFKey])
        }

        
    }

    obj["stats"] = stats;

    return obj
}




/*------ Method for read uploded csv file ------*/
function upload() {
    let input = document.getElementById('csvFile');
    input.addEventListener('change', function() {
    
    var formdata = form();
    if (this.files && this.files[0]) {

        var myFile = this.files[0];
        var reader = new FileReader();
        
        reader.addEventListener('load', function (e) {
            
            let csvdata = e.target.result; 
            sendData(csvdata, formdata)
            // parse(csvdata); // calling function for parse csv data 
        });
        
        reader.readAsBinaryString(myFile);
        
    }
    });
}

/*------- Method for parse csv data and display --------------*/
// function parse(data) {

//     let parsedata = [];

//     let newLinebrk = data.split("\n");
//     for(let i = 0; i < newLinebrk.length; i++) {

//         parsedata.push(newLinebrk[i].split(","))
//     }

//     console.table(parsedata)
// }

async function sendData(csvdata, formdata) {
    payload = {
        data: csvdata,
        title: formdata.title,
        description: formdata.description,
        local: formdata.local,
        stats: formdata.stats
    }

    $.ajax({
        type: "POST",
        url: "/upload",
        contentType: "application/json",
        data: JSON.stringify(payload),
        success: function(res) {
            console.log(res);
            window.location.replace(window.location.origin + res)
        }
    });
} 

upload()