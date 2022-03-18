//创建路由器
import VueRouter from 'vue-router'

import Catalogue from '../components/Catalogue'
import Schedule from '../components/Schedule'
import Booklist from '../components/Booklist'
import Sign from '../components/Sign'
import Skill from '../components/Skill'
import docx from '../components/docx'
import Excerptlist from '../components/Excerptlist'
import Websitemarks from '../components/Websitemarks'
import Collect from '../components/Collect'


//创建路由器
export default new VueRouter({
    routes:[
        {
            path:'/catalogue',
            component:Catalogue
        },
        {
            path:'/schedule',
            component:Schedule

        },
        {
            path:'/booklist',
            component:Booklist
        },
        {
            path:'/signin',
            component:Sign

        },
        {
            path:'/skill',
            component:Skill
        },
        {
            path:'/detail',
            component:docx
        },
        {
            path:'/excerptlist',
            component:Excerptlist
        },
        {
            path:'/web',
            component:Websitemarks

        },
        {
            path:'/collect',
            component:Collect
        }
    ]
})