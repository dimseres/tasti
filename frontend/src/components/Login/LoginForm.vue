<template>
  <div>
    <div class="login__input">
      <div class="form__input">
        <BaseInput v-model="login" placeholder="Email"/>
      </div>
    </div>
    <div class="login__input">
      <div class="form__input">
        <BaseInput v-model="password" type="password" placeholder="Пароль"/>
      </div>
    </div>
    <div class="login__action">
        <a href="#" class="button__login" @click="auth">Войти</a>
      </div>
  </div>
</template>

<script>
import BaseInput from "../UI/BaseInput";

export default {
  name: "RegistrationForm",
  components: {BaseInput},
  data() {
    return {
      login: null,
      password: null
    }
  },
  methods: {
    async auth() {
      await this.axios.post('auth/', {
        username: this.login,
        password: this.password
      }).then(data => {
        console.log(data)
      })
    }
  }
}
</script>

<style scoped>

</style>