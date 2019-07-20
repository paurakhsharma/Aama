<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12 col-lg-7 main">
        <div class="form">
          <h3 class="mb-5 text-center">Aama's Details</h3>

          <form action="insert.php" method="get">
            <div class="form-group row">
              <label for="age" class="col-sm-3 col-form-label">Age</label>
              <div class="col-sm-9">
                <input type="number" name="age" class="form-control" id="age" placeholder="Age" />
              </div>
            </div>

            <div class="form-group row">
              <label for="delNo" class="col-sm-3 col-form-label">Delivery Number</label>
              <div class="col-sm-9">
                <input
                  type="number"
                  name="delNo"
                  class="form-control"
                  id="delNo"
                  placeholder="Delivery Number"
                />
              </div>
            </div>

            <div class="form-group row">
              <label for="post" class="col-sm-3 col-form-label">Delivery Time</label>
              <div class="col-sm-9">
                <select name="post" class="form-control" id="time">
                  <option value>Select Time</option>
                  <option value="CEO">Premature</option>
                  <option value="Team Leader">Mature</option>
                  <option value="Members">Late Comer</option>
                </select>
              </div>
            </div>

            <div class="form-group row">
              <label for="post" class="col-sm-3 col-form-label">Blood Pressure</label>
              <div class="col-sm-9">
                <select name="post" class="form-control" id="pressure">
                  <option value>Select Blood Pressure</option>
                  <option value="CEO">Low</option>
                  <option value="Team Leader">Normal</option>
                  <option value="Members">High</option>
                </select>
              </div>
            </div>

            <div class="form-group row">
              <label for="heartRate" class="col-sm-3 col-form-label">Heart Rate</label>
              <div class="col-sm-9">
                <input
                  type="number"
                  name="heartRate"
                  class="form-control"
                  id="heartRate"
                  placeholder="Heart Rate"
                />
              </div>
            </div>

            <div class="text-center mt-5 pt-5">
              <button type="reset" class="btn btn-outline-warning mr-1">Reset</button>
              <button type="submit" class="btn btn-outline-success mr-1">Submit</button>
            </div>
          </form>
        </div>
      </div>

      <div class="col-5 side d-none d-lg-block">
        <!-- <p class="text-center"></p> -->
        <div class="row b">
          <div class="col-5 text-right">
            <img class="logo" src alt />
          </div>
          <div class="col-6 logo-p">
            Aaama
            <br />
          </div>
        </div>

        <img class="img" src="@/assets/texture.png" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Aama",
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@import url("https://fonts.googleapis.com/css?family=Varela+Round");

body {
  font-family: "Varela Round", sans-serif !important;
}

.side {
  background-image: linear-gradient(to bottom, #434343 0%, black 100%);
  height: 98vh;
  padding-left: 0 !important;
  padding-right: 0 !important;
  margin: 0;
  display: inline-block;
}

.b {
  margin-top: 30%;
}
.side .img {
  max-width: 100%;
  max-height: 100%;
  position: absolute;
  bottom: 0;
}
.side .logo {
  width: 60px;
  margin: 10px;
}
.logo-p {
  font-size: 30px;
  color: #ffffff;
}
.logo-c {
  max-width: 50%;
}

.main {
  background-color: #eeeeee;
  height: 100vh;
  margin: 0;
  padding: 0;
}

.main .form {
  margin-top: 10%;
  margin-left: 5%;
  margin-right: 5%;
  background: #ffffff;
  border-radius: 20px;
  padding: 3% 8%;
}
input[type="text"] select {
  width: 100%;
  padding: 12px 10px;
  border: none;
  border-radius: 0;
  border-bottom: 2px solid rgb(126, 126, 126);
  overflow-x: hidden !important;
}
input[type="text"]:focus select:active {
  outline: none;
  box-shadow: none !important;
  /* border:0px solid #ccc !important; */
  border-bottom: 2px solid rgb(0, 0, 0);
}
</style>
