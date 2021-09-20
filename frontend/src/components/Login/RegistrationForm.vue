<template>
  <div>
      <div class="login__input">
        <div class="form__input">
          <BaseInput v-model="login" placeholder="Имя"/>
        </div>
        <div class="form__input">
          <BaseInput v-model="login" placeholder="Email"/>
        </div>
        <div class="form__input">
          <BaseInput v-model="password" placeholder="Пароль" type="password"/>
        </div>
        <div class="form__input offert">
          <input id="offert" type="checkbox" placeholder="Пароль"/>
          <label for="offert" class="offer__label">соглас(ен/на) с правилами и политикой конфедициальности</label>
        </div>
      </div>
      <div class="login__action">
        <a href="#" class="button__login">Зарегистрироваться</a>
        <router-link :to="{name: 'Login'}" class="button__signin">Войти</router-link>
      </div>
  </div>
</template>

<script>
import BaseInput from "../UI/BaseInput";

export default {
  name: "LoginForm",
  components: {BaseInput},
  data() {
    return {
      login: "",
      password: ""
    }
  }
}
</script>

<style scoped lang="scss">

</style>