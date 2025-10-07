
Rails.application.routes.draw do
  root "home#index"   # your home page
  resources :blogs    # adds blog routes
end
