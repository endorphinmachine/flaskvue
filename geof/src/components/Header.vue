<template>
<div class='Header'>
    <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand href="/">首页</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">link1</b-nav-item>
        <b-nav-item href="#">link2</b-nav-item>
        <b-nav-item href="#">link3</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <b-nav-item-dropdown text="###" right>
          <b-dropdown-item href="#">##</b-dropdown-item>
          <b-dropdown-item href="#">##</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <font size="3" face="华文中宋">用户中心</font>
          </template>
          <b-dropdown-item href="/#/login">登录</b-dropdown-item>
          <b-dropdown-item href="/#/register">注册</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>
<script>
export default {
}
</script>
<style scoped>

</style>
