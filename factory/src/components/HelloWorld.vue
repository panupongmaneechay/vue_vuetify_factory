<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-h6">Master Parts Changeover matrix</v-card-title>
          <v-card-text>
            <p>Hello {{ username }}!</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    username: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
/* Add any custom styles if needed */
</style>
