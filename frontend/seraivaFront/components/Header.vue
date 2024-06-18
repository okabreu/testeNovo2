<script setup lang="ts">
import { ref } from 'vue';

const itensMenu = ref([
    {
        label: 'Home',
        icon: 'pi pi-home',
    },
    {
        label: 'Pagamentos',
        icon: 'pi pi-wallet'
    },
    {
        label: 'Login',
        icon: 'pi pi-user'
    },
    {
    label: "Meus pedidos",
    icon: "pi pi-briefcase",
    },
]);

const painel = ref();

const toggle = (event: any) => {
    painel.value.toggle(event);
}

</script>
  

<template>
    <header>
    <div class="flex align-items-center justify-content-center">
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-home mr-1"></i>
          <NuxtLink to="/">Livros</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-user mr-1"></i>
          <NuxtLink to="/login">Login</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-shopping-cart mr-1"></i>
          <NuxtLink to="/carrinho">Carrinho</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-shopping-bag mr-1"></i>
          <NuxtLink to="/pedidos">Pedidos</NuxtLink>
        </div>

        <div class="chatbot">
            <Button type="button" icon="pi pi-comment" label="Chatbot" @click="toggle" />
            <OverlayPanel ref="painel">
                <iframe allow="microphone;" width="350" height="430"
                    src="https://console.dialogflow.com/api-client/demo/embedded/8c5075cc-4b7f-4065-9055-66462508fbac">
                </iframe>
            </OverlayPanel>
        </div>
    </div>

    

    </header>
</template>

<style scoped lang="scss">
    header{
        width: 100vw;
        height: var(--altura-header);
        background-color: #8FD9BE;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.318);
        border-bottom: 1rem solid #02735E;
        position: fixed, absolute;

        .menu-item{
            height: var(--altura-header);
    
                a{
                text-decoration: none;
                color: #ffffff;
                }
                
                &:hover{
                transform: scale(1.1);
                }
    }
    .chatbot{
    top: 0;
    right: 0;
    margin: 1rem
}
}


</style>