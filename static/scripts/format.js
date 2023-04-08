var colbtn = document.getElementById("add-col");
colbtn.addEventListener("click", addCol);

document.addEventListener("click", function (event) {
  const target = event.target.closest("#add-stat");
  var box = event.target.closest('#col-stat-box');

// ITERATING OVER THE FORM
//   for( var i=0; i<document.forms.dataInput.elements.length; i++ )
// {
//    var fieldName = document.forms.dataInput.elements[i].name;
//    var fieldValue = document.forms.dataInput.elements[i].value;

//    console.log(fieldName + ": " + fieldValue)
// }


  if (target) {
    addStat(box);
  }
});

function addCol() {
  var e = document.createElement("div");
  e.innerHTML = `
  <div class="row" id="col-stat-box">
  <div class="col-sm-6">
      <label for="columnTitle" class="form-label mt-2">Field Name</label>
      <input
        type="text"
        class="form-control"
        id="columnTitle"
        placeholder="Field one"
        name="col_name"
      />

      <div id="add-stat-btn" class="mt-2">
        <button type="button" class="btn btn-outline-dark" id="add-stat">Add Stat</button>
      </div>
  </div>
  <div class="col-sm-6" id="stat-box">
      <label for="stat-choice" class="form-label mt-2">Statistic</label>
      <select class="form-select" aria-label="Default select" id="stat-choice" name="stat_choice">
          <option selected="">Choose a stat</option>
          <option value="bounded_mean">Bounded Mean</option>
          <option value="bounded_sum">Bounded Sum</option>
          <option value="median">Median</option>
          <option value="min">Minimum</option>
          <option value="max">Maximum</option>
          <option value="standard_deviation">Standard Deviation</option>
          <option value="variance">Variance</option>
        </select>
      <label for="epsilon" class="form-label mt-2">Epsilon</label>
      <input
        type="number"
        class="form-control"
        id="epsilon"
        placeholder="0.5"
        name="epsilon"
      />
      <label for="low" class="form-label mt-2">Low</label>
      <input
        type="number"
        class="form-control"
        id="low"
        placeholder="0"
        name="low"
      />
      <label for="high" class="form-label mt-2">High</label>
      <input
        type="number"
        class="form-control"
        id="high"
        placeholder="1000"
        name="high"
      />
  </div>
</div>`;
  var btn = document.getElementById("add-col-btn");
  while (e.firstChild) {
    btn.appendChild(e.firstChild);
  }
}

function addStat(box) {
  var e = document.createElement("div");
  e.innerHTML = `
  <div class="col-sm-6"></div>
  <div class="col-sm-6">
  <label for="stat-choice" class="form-label mt-2">Statistic</label>
  <select class="form-select" aria-label="Default select" id="stat-choice" name="stat_choice">
      <option selected="">Choose a stat</option>
      <option value="bounded_mean">Bounded Mean</option>
      <option value="bounded_sum">Bounded Sum</option>
      <option value="median">Median</option>
      <option value="min">Minimum</option>
      <option value="max">Maximum</option>
      <option value="standard_deviation">Standard Deviation</option>
      <option value="variance">Variance</option>
    </select>
  <label for="epsilon" class="form-label mt-2">Epsilon</label>
  <input
    type="number"
    class="form-control"
    id="epsilon"
    placeholder="0.5"
    name="epsilon"
  />
  <label for="low" class="form-label mt-2">Low</label>
  <input
    type="number"
    class="form-control"
    id="low"
    placeholder="0"
    name="low"
  />
  <label for="high" class="form-label mt-2">High</label>
  <input
    type="number"
    class="form-control"
    id="high"
    placeholder="1000"
    name="high"
  />
  </div>`;

  // var btn = document.getElementById('stat-box')
  while (e.firstChild) {
    box.appendChild(e.firstChild);
  }
}
