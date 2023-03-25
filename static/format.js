var btn = document.getElementById('add-stats')
btn.addEventListener('click', addStat)

function addStat() {
    var e = document.createElement('div');
    e.innerHTML = `
    <div class="container-fluid">
  <div class="row">
      <div class="col-sm-6">
          <label for="columnTitle" class="form-label mt-2">Column title</label>
          <input
            type="text"
            class="form-control"
            id="columnTitle"
            placeholder="Column name"
          />
      </div>
      <div class="col-sm-6">
          <label for="stat-choice" class="form-label mt-2">Statistic</label>
          <select class="form-select" aria-label="Default select" id="stat-choice">
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
          />
          <label for="low" class="form-label mt-2">Low</label>
          <input
            type="number"
            class="form-control"
            id="low"
            placeholder="0"
          />
          <label for="high" class="form-label mt-2">High</label>
          <input
            type="number"
            class="form-control"
            id="high"
            placeholder="1000"
          />
      </div>
  </div>
</div>`
    var btn = document.getElementById('add-btn')
    while(e.firstChild) {
        btn.appendChild(e.firstChild)
    }

}