<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" sm="8" md="6">
          <v-btn @click="openAddPartModal" color="primary">Add Part</v-btn>
          <v-data-table :headers="headers" :items="data" class="elevation-1">
            <!-- eslint-disable-next-line vue/valid-v-slot -->
            <template v-slot:item.editTime="{ item: rowData }">
              <td>
                <v-btn @click="openEditModal(rowData)" color="primary" outlined small>
                  Edit
                </v-btn>
              </td>
            </template>
          </v-data-table>
  
          <v-dialog v-model="addPartModal" max-width="600px">
            <!-- Add Part Modal Content -->
          </v-dialog>
  
          <v-dialog v-model="editModal" max-width="600px">
            <v-card>
              <v-card-title>Edit Time</v-card-title>
              <v-card-text>
                <v-form @submit.prevent="saveEdit">
                  <v-row v-for="part in editedItem.parts" :key="part.name">
                    <v-col>
                      <v-text-field v-model="part.value" :label="part.name"></v-text-field>
                    </v-col>
                  </v-row>
                  <v-btn type="submit" color="primary">Save</v-btn>
                </v-form>
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
      headers: [
        { text: 'Part', align: 'start', value: 'name' },
        { text: 'Part A', value: 'parts[0].value' },
        { text: 'Part B', value: 'parts[1].value' },
        { text: 'Part C', value: 'parts[2].value' },
        { text: 'Edit Time', value: 'editTime' },
      ],
      data: [],
      addPartModal: false,
      editModal: false,
      editedItem: {
        name: '',
        parts: [],
      },
    };
  },
  methods: {
    openAddPartModal() {
      this.addPartModal = true;
    },
    openEditModal(item) {
      this.editedItem = { ...item };
      this.editModal = true;
    },
    async fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/data/part_all');
        this.data = response.data; // Assuming the API returns an array of objects similar to your existing 'data' structure
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    saveAddPart() {
      // Implement saveAddPart logic
    },
    saveEdit() {
      // Implement saveEdit logic
      this.editModal = false;
    },
  },
  mounted() {
    // Fetch data when the component is mounted
    this.fetchData();
  },
};
</script>

  
  <style scoped>
  /* Add any custom styles if needed */
  </style>
  