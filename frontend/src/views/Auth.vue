<template>
  <div class="auth">
    <div class="auth__wrapper">
      <div class="login__form">
        <div class="login__header">
          <h2 class="login__title">Авторизация</h2>
          <div class="login__tabs">
            <router-link :to="{name: 'Registration'}" href="" class="tab__item">Регистрация</router-link>
            <router-link :to="{name: 'Login'}" href="" class="tab__item">Вход</router-link>
          </div>
        </div>
        <div class="login__socials">
      <span class="social__title">
        Вы можете войти через
      </span>
          <div class="socials__wrapper">
            <a href="#" class="auth__social"><img src="/icons/32px/vk.svg" alt="#"></a>
            <a href="#" class="auth__social"><img src="/icons/32px/google.svg" alt="#"></a>
          </div>
        </div>
        <div class="login__input__wrapper">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Auth",
}
</script>

<style scoped lang="scss">
.auth {
  background: #FAFAFA;
  display: flex;
  min-width: 100vw;
  min-height: 100vh;
  justify-content: center;
  align-items: center;

  &__wrapper {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    height: 500px;
  }
}

.login {
  &__header {
    border-bottom: 1px solid $color_gray_light;
    padding: 32px 32px 0px 32px;
  }

  &__form {
    background: #fff;
    width: 474px;
    display: flex;
    flex-direction: column;
    box-shadow: 0px 4px 4px rgba(51, 51, 51, 0.04), 0px 4px 16px rgba(51, 51, 51, 0.08);
    border-radius: 8px;
  }

  &__title {
    font-family: 'Montserrat';
    margin: 0 0 32px 0;
    font-weight: 900;
    font-size: 32px;
  }

  &__input {
    display: flex;
    flex-direction: column;
  }

  &__wrapper {
    padding: 32px;
  }

  &__socials {
    background: #fafafa;
    padding: 12px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__input__wrapper {
    padding: 0px 32px 32px 32px;
  }

  &__tabs {
    display: flex;

    .tab__item {
      padding-bottom: 32px;
      margin-right: 20px;
      display: block;
      position: relative;
      transition: .2s;
      color: $color_gray_dark;

      &::after {
        content: "";
        display: block;
        position: absolute;
        bottom: 0px;
        width: 100%;
        height: 2px;
        background: transparent;
        transition: .2s;
      }

      &:hover {
        &::after {
          background: $color_primary;
        }
      }
    }

    & .router-link-exact-active {
      color: $color_black;

      &::after {
        background: $color_primary;
      }
    }
  }
}

.social__title {
  font-size: 13px;
}

.socials__wrapper {
  display: flex;
}

.auth__social {
  border-radius: 50%;
  background: #fff;
  padding: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
  //width: 36px;
  //height: 36px;
  margin-left: 8px;
}
</style>