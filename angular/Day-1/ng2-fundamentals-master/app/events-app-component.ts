import {Component} from '@angular/core/';

@Component({
    selector:   'events-app',
    template:   `
   <div><pm-products></pm-products></div>
    
    `
})

export class EventsAppComponent{
    name : string = "ABC";
}