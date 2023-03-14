    /*------ Method for read uploded csv file ------*/
function upload() {
       
    let input = document.getElementById('csvFile');
    input.addEventListener('change', function() {

    if (this.files && this.files[0]) {

        var myFile = this.files[0];
        var reader = new FileReader();
        
        reader.addEventListener('load', function (e) {
            
            let csvdata = e.target.result; 
            sendData(csvdata)
            // parse(csvdata); // calling function for parse csv data 
        });
        
        console.log(reader.readAsBinaryString(myFile));
        
    }
    });
}

/*------- Method for parse csv data and display --------------*/
function parse(data) {

    let parsedata = [];

    let newLinebrk = data.split("\n");
    for(let i = 0; i < newLinebrk.length; i++) {

        parsedata.push(newLinebrk[i].split(","))
    }

    console.table(parsedata)
}

async function sendData(data) {
    payload = {
        user_id: "12345",
        data: data,
        private: false,
        description: "Medical data from UNC hospital",
        author: "Matthew Gilmore",
        local: false,
        stats: {
            "age": ["bounded_mean", "max", "min"],
            "height": ["bounded_mean", "max", "min", "standard_deviation"],
            "weight": ["bounded_mean", "max", "min"]
        }
    }

    $.ajax({
        type: "POST",
        url: "/upload",
        contentType: "application/json",
        data: JSON.stringify(payload),
        dataType: "json",
        success: function(response) {
            console.log(response);
        },
        error: function(err) {
            console.log(err);
        }
    });
} 

upload()