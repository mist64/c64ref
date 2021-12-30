
import { Application , send } from 'Oak';

const
    { log } = console,
    { now } = Date;

const path = new URL('.',import.meta.url)
    .pathname.replace('%20',' ');

const
    root = `${ path }../Source/`,
    index = 'index.html',
    port = 6464;


log(`Starting C64Ref Test Server`);
log(`===========================`);

const server = new Application;
server.use(Logger);
server.use(Timer);
server.use(Files);
await server.listen({ port });


/*
 *      Logger
 */

async function Logger(context,next){

    await next();

    const { request , response } = context;
    const { method , url } = request;

    const delta = response.headers.get('X-Response-Time');
    const path = url.pathname.slice(1);

    log(`〈 ${ method } 〉 ⸢ ${ delta } ⸥  ${ path }`);
}


/*
 *      Timer
 */

async function Timer(context,next){

    const before = now();

    await next();

    const delta = now() - before;

    const { headers } = context.response;

    headers.set('X-Response-Time',`${ delta }ms`);
}


/*
 *      Files
 */

async function Files(context){
    const { pathname } = context.request.url;
    await send(context,pathname,{ root , index });
}
