<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12 col-lg-7 main">
        <div class="form">
          <h3 class="mb-5 text-center">Aama's Details</h3>

          <form @submit.prevent="predict">
            <div class="form-group row">
              <label for="age" class="col-sm-3 col-form-label">Age</label>
              <div class="col-sm-9">
                <input 
                  type="number"
                  name="age"
                  class="form-control"
                  id="age"
                  placeholder="Age"
                  v-model="age" />
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
                  v-model="deliveryN"
                />
              </div>
            </div>

            <div class="form-group row">
              <label for="post" class="col-sm-3 col-form-label">Delivery Time</label>
              <div class="col-sm-9">
                <select name="post" class="form-control" id="time" v-model="deliveryT">
                  <option value>Select Time</option>
                  <option value="0">Timely</option>
                  <option value="1">Premature</option>
                  <option value="2">Late Comer</option>
                </select>
              </div>
            </div>

            <div class="form-group row">
              <label for="post" class="col-sm-3 col-form-label">Blood Pressure</label>
              <div class="col-sm-9">
                <select name="post" class="form-control" id="pressure" v-model="blood">
                  <option disabled value="">Select Blood Pressure</option>
                  <option value="0">Low</option>
                  <option value="1">Normal</option>
                  <option value="2">High</option>
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
                  v-model="heart"
                />
              </div>
            </div>

            <div class="text-center mt-5 pt-5">
              <button type="reset" class="btn btn-outline-warning mr-1">Reset</button>
              <button type="submit" class="btn btn-outline-success mr-1" @click.prevent='predict'>Submit</button>
            </div>
          </form>
        </div>
      </div>

      <div class="col-5 side d-none d-lg-block">
        <!-- <p class="text-center"></p> -->
        <div class="row b">
          <div class="col-5 text-left">
            <!-- <img class="logo" src alt /> -->
          </div>
          <div>
            <div v-if="survived" style="margin-left: 150px">
            <div class="col-8 logo-p text-dark">
              Needs C-Section
              <img src="@/assets/csection.png"  class="result-img" alt="">
            </div>
            </div>
            <div v-if="notSurvived">
              <div class="col-6 logo-p text-dark to-left">
                Normal Delivery
              </div>
              <img src="@/assets/no_csection.png" style="margin-left:-60px" class="result-img" alt="">
            </div>
          </div>
        <img class="img" src="@/assets/texture.png" />
      </div>
    </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = 'http://localhost:5000'

export default {
  name: "Aama",
  data() {
    return {
      prediction: '',
      age: '',
      deliveryN: '',
      deliveryT: '',
      blood: '',
      heart: ''
    }
  },
  methods: {
    predict() {
      console.log(this.age)
      console.log(this.deliveryN)
      console.log(this.deliveryT)
      console.log(this.blood)
      console.log(this.heart)
      this.axios
        .post(`${SERVER_URL}/predict`, [
          {
            "Age": parseInt(this.age),
            "DeliveryN": parseInt(this.deliveryN),
            "DeliveryT": parseInt(this.deliveryT),
            "Blood": parseInt(this.blood),
            "Heart": parseInt(this.heart)
          }
        ])
        .then((response) => {
          console.log(response.data.predictions)
          this.prediction = parseInt(response.data.predictions)
      })
    }
  },
  computed: {
    survived() {
      return this.prediction === 1
    },
    notSurvived() {
      return this.prediction === 0
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@import url("https://fonts.googleapis.com/css?family=Varela+Round");

body {
  font-family: "Varela Round", sans-serif !important;
}

.side {
  /* background-image: linear-gradient(to bottom, #434343 0%, black 100%); */
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
  font-size: 25px;
  width: 100px;
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



/* .to-left {
  margin-left: -75px;
} */

/* .result {
  position: relative;
} */

.result-img {
  width: 250px;
  height: auto;

} 
</style>
