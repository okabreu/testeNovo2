<script setup lang="ts">
import Password from 'primevue/password';
import { reactive, ref } from 'vue';
const { signIn } = useAuth();


definePageMeta({
    layout: 'login'
});

const credenciais = reactive({
    email: '',
    password: ''
});
const mensagemErro = ref('');

const fazerLogin = async () => {
    console.log("login: ", credenciais);
    try {
        const usuario = await signIn(credenciais, { redirect: false });
        console.log("logado com sucesso!", usuario);

        if (usuario.groups === 'Bibliotecário') {
            console.log("logado com sucesso!");
            navigateTo('/');
        } else {
            mensagemErro.value = 'Você não tem permissão para acessar este sistema.';
            setTimeout(() => {
                mensagemErro.value = '';
                credenciais.email = '';
                credenciais.password = '';
            }, 3000);
        }
    } catch (error) {
        console.error("error: ", error);
        mensagemErro.value = 'Não foi possivel fazer o login com essas credenciais...';
        setTimeout(() => {
            mensagemErro.value = '';
            credenciais.email = '';
            credenciais.password = '';
        }, 3000);
    }
}
</script>

<template>
    <main class="login-main flex align-items-center justify-content-center">
        <section class="login-container flex flex-column align-items-center justify-content-center">
            <h4 class="row-login">LOGIN</h4>
            <div class="row-login">
                <FloatLabel>
                    <InputText v-model="credenciais.email" type="email" id="email-input" class="input-text"/>
                    <label for="email-input">Email</label>
                </FloatLabel>
            </div>
            <div class="row-login">
                <FloatLabel>
                    <InputText v-model="credenciais.password" type="password" id="password-input" class="input-text"/>
                    <label for="password-input">Senha</label>
                </FloatLabel>
            </div>
            <div class="row-login" v-if="mensagemErro !== ''">
                <p id="erro">{{  mensagemErro }}</p>
            </div>
            <div class="row-login">
                <Button @click="fazerLogin" label="LOGIN" id="login-button"></Button>
            </div>
        </section>
    </main>
</template>

<style scoped lang="scss">
.login-main{
    h1{
        color: lavender;
    }
    width: 100vw;
    height: 100vh;
    background: rgb(143,217,190);
    background: radial-gradient(circle, rgba(143,217,190,1) 0%, rgba(2,115,94,1) 100%);

    .login-container{
        width: 30vw;
        height: 70vh;
        border-radius: 3vh;
        background-color: rgb(255, 255, 255);

        .row-login{
            margin: 1rem 0 1rem 0;
            .input-text{
                height: 2rem;
                width:  200px;
            }

            #login-button{
                width: 200px;
                height: 2rem;
                background-color: #034C8C;
                border: 0px;
            }

            #erro{
                color: tomato;
                font-size: 0.8rem;
            }
        }
    }
}
</style>
