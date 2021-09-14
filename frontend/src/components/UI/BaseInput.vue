<template>
  <input
      class="input"
      :value="modelValue"
      :type="type"
      :min="min"
      :max="max"
      :disabled="disabled"
      :placeholder="placeholder"
      @input="updateInput"
  >
</template>

<script>
export default {
  name: "BaseInput",
  props: [
    'type',
    'modelValue',
    'min',
    'max',
    'disabled',
    'placeholder'
  ],
  data() {
    return {}
  },
  methods: {
    updateInput(event) {
      this.$emit("update:modelValue", event.target.value);
    }
  }
}
</script>

<style scoped lang="scss">
.input {
  width: 100%;
  box-shadow: 0px 4px 4px rgba(51, 51, 51, 0.04), 0px 4px 16px rgba(51, 51, 51, 0.08);
  border-radius: 4px;
  padding: 16px;
  outline: none;
  border: none;
}
</style>