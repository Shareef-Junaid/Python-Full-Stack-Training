import {NgModule} from '@angular/core'

import {BrowserModule} from '@angular/platform-browser'

import {EventsAppComponent} from './events-app-component'
import { ProductListComponent } from './products/product-list.component';
import { ConvertToSpacesPipe } from './convertToSpaces.pipe';
import { StarComponent } from './star/star.component';

@NgModule({
    imports: [BrowserModule],
    declarations: [EventsAppComponent,ProductListComponent,ConvertToSpacesPipe,StarComponent],
    bootstrap: [EventsAppComponent]
})

export class AppModule{
}