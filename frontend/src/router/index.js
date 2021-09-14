import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: "/",
        name: "Home",
        component: () => import('../views/Home'),
        children: [
            {
                path: '/',
                name: 'Courses',
                component: () => import('../pages/Courses')
            },
            {
                path: "/components",
                name: "Components",
                component: () => import('../views/Components')
            },
        ]
    },
    {
        path: "/auth",
        name: "Auth",
        component: () => import('../views/Auth'),
        children: [
            {
                path: '',
                name: 'Login',
                component: () => import('../components/Login/LoginForm')
            },
            {
                path: '/register',
                name: 'Registration',
                component: () => import('../components/Login/RegistrationForm')
            },
        ]
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
