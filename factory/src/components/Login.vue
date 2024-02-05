<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" sm="8" md="4">
          <v-card>
            <v-card-title class="text-h5">Login</v-card-title>
            <v-card-text>
              <v-form @submit.prevent="login">
                <v-text-field v-model="username" label="Username" required></v-text-field>
                <v-text-field v-model="password" label="Password" type="password" required></v-text-field>
                <v-btn type="submit" color="primary">Login</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    name: 'LoginComponent',
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      login() {
        if (this.username === 'admin123' && this.password === 'admin123') {
          // Redirect to the Hello page and pass the username as a prop
          this.$router.push({ name: 'index', params: { username: this.username } });
        } else {
          // Display an error message or handle the login failure
          this.$bvToast.toast('Invalid credentials. Please try again.', {
            title: 'Error',
            variant: 'danger',
          });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add any custom styles if needed */
  </style>
  