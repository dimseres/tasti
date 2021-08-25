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
            }
        ]
    },

];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
